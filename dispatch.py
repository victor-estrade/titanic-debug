# coding: utf-8

import os
import datetime

from template import SBATCH_TEMPLATE

from uuid import uuid4

from subprocess import call


"""
Role = lancer les scripts de test sur les divers noeuds.
"""

BALTIC_NODES = ["baltic-1"]

TITANIC_NODES = [
            "titanic-1",
            "titanic-2",
            "titanic-3",
            "titanic-4",
            "titanic-5",
            ]

REPUBLIC_NODES = [
            "republic-1",
            "republic-2",
            "republic-3",
            "republic-4",
            "republic-5",
            "republic-6",
            "republic-7",
            ]

NODE_LIST = TITANIC_NODES + REPUBLIC_NODES + BALTIC_NODES


def launch_on_all_nodes():
    for node_name in NODE_LIST:
        launch_on_node(node_name)


def launch_on_node(node_name):
    logdir = generate_unique_logdir(node_name)
    script = fill_template(node_name, logdir)
    script_path = os.path.join(logdir, 'script.slurm')
    write_script(script, logdir, script_path)
    run_one_script(script_path)

def generate_unique_logdir(node_name):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    job_name = f"DEAD-{node_name[0]}{node_name[-1]}"
    workdir = os.getcwd()
    logdir = os.path.join(workdir, 'log', job_name, now)
    return logdir


def fill_template(node_name, logdir):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    node_list = node_name
    job_name = f"DEAD-{node_name[0]}{node_name[-1]}"
    workdir = os.getcwd()
    max_time = "1-00:00:00"
    cpu = 6
    memory = '64g'
    partition = 'besteffort'
    gpu = 1
    node_list = node_list
    docker_image = 'estradevictorantoine/systml:1.5'
    benchmark = "run.torch_net"
    main_args = ""

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


def run_one_script(script_path):
    # Start job
    cmd = ['sbatch', script_path]
    print(" ".join(cmd))
    call(cmd)
