# coding: utf-8

import os

from uuid import uuid4


"""
Role = lancer les scripts de test sur les divers noeuds.
"""

TITANIC_NODES = [
            "titanic-1",
            "titanic-2",
            "titanic-3",
            "titanic-4",
            "titanic-5",
            ]
REPUBLIC_NODES
REPUBLIC_NODES = [
            "republic-1",
            "republic-2",
            "republic-3",
            "republic-4",
            "republic-5",
            "republic-6",
            ]

NODE_LIST = TITANIC_NODES + REPUBLIC_NODES


def fill_template(node_list):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    job_name = "DEAD"
    root_logdir = args.logdir
    logdir = os.path.join(root_logdir, job_name, now)
    max_time = args.max_time
    cpu = args.cpu
    memory = args.mem
    partition = args.partition
    gpu = args.gpu
    node_list = node_list
    docker_image = args.docker_image
    benchmark = args.benchmark

    container_name = str(uuid4())[:8]

    log_stdout = os.path.join(logdir, '%A_%a.stdout')
    log_stderr = os.path.join(logdir, '%A_%a.stderr')
    script_path = os.path.join(logdir, 'script.slurm')


    script = SBATCH_TEMPLATE.format(**locals())
    return script


def write_script(script, logdir, script_path):
    os.makedirs(logdir, exist_ok=True)
    with open(script_path, "w") as file:
        print(script, file=file)


def run(script_path):
    # Start job
    cmd = ['sbatch', script_path]
    print(" ".join(cmd))
    call(cmd)
