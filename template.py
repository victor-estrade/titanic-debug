


SBATCH_TEMPLATE = \
"""#!/bin/bash
#SBATCH --account=tau
#SBATCH --array={array}%10
#SBATCH --job-name={xp_name}
#SBATCH --output={log_stdout}
#SBATCH --error={log_stderr}
#SBATCH -t {max_time}             # max runtime days-hours:min:sec
#SBATCH --cpus-per-task={cpu}
#SBATCH --mem={memory}
#SBATCH --partition={partition}
#SBATCH --gres=gpu:{gpu}
#SBATCH --exclude=baltic-1,republic-3,republic-1,titanic-4,titanic-1

# test --exclude=baltic-1,republic-[1-2],republic-[4-6],titanic-[1-5]
# republic-3 is working  !

hostname

export TMPDIR=$HOME/tmp

function dockerkill
{{
    echo "Killing docker {container_name}_${{SLURM_ARRAY_TASK_ID}}"
    docker kill {container_name}_${{SLURM_ARRAY_TASK_ID}}
    echo "Cancelling job ${{SLURM_JOB_ID}}_${{SLURM_ARRAY_TASK_ID}}"
    scancel "${{SLURM_JOB_ID}}_${{SLURM_ARRAY_TASK_ID}}"
}}

trap dockerkill TERM
trap dockerkill INT
trap dockerkill CONT

GRID_PARAMS=$(cat {parameters_file} | head -n $SLURM_ARRAY_TASK_ID | tail -n 1)
WORKDIR="/home/tao/vestrade/workspace/SystML/SystGradDescent"

echo "SLURM_ARRAY_TASK_ID"
echo $SLURM_ARRAY_TASK_ID

echo "GRID_PARAMS"
echo "${{GRID_PARAMS}}"

sdocker -i  -v /home/tao/vestrade/datawarehouse:/datawarehouse \
            -v $WORKDIR:$WORKDIR --name "{container_name}_${{SLURM_ARRAY_TASK_ID}}" \
            {docker_image} \
            bash -c "cd ${{WORKDIR}}; python -m {benchmark} {main_args} ${{GRID_PARAMS}}"
"""
