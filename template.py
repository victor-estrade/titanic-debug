# coding: utf-8



SBATCH_TEMPLATE = \
"""#!/bin/bash
#SBATCH --account=tau
#SBATCH --job-name={job_name}
#SBATCH --output={log_stdout}
#SBATCH --error={log_stderr}
#SBATCH -t {max_time}             # max runtime days-hours:min:sec
#SBATCH --cpus-per-task={cpu}
#SBATCH --mem={memory}
#SBATCH --partition={partition}
#SBATCH --gres=gpu:{gpu}
#SBATCH --nodelist={node_list}

hostname

export TMPDIR=$HOME/tmp

function dockerkill
{{
    echo "Killing docker {container_name}"
    docker kill {container_name}
    echo "Cancelling job ${{SLURM_JOB_ID}}"
    scancel "${{SLURM_JOB_ID}}"
}}

trap dockerkill TERM
trap dockerkill INT
trap dockerkill CONT

WORKDIR={workdir}


sdocker -i  -v $WORKDIR:$WORKDIR \
            --name "{container_name}" \
            {docker_image} \
            bash -c "cd ${{WORKDIR}}; python -m {benchmark} {main_args}"
"""
