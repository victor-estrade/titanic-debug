# coding: utf-8

import os
import datetime
import glob

from dispatch import NODE_LIST
from run.common import END_MSG



def evaluate_all():
    for node_name in NODE_LIST:
        dead_status = is_dead(node_name)
        if dead_status is None:
            print(f"[NONE] {node_name}")
        elif dead_status:
            print(f"[DEAD] {node_name}")
        else:
            print(f"[ALIVE] {node_name}")


def is_dead(node_name):
    fname = latest_out_file(node_name)
    if fname:
        end_msg = get_end_msg(fname)
        print("end_msg ====")
        print(end_msg)
        return end_msg != END_MSG
    else:
        return None



def latest_out_file(node_name):
    job_name = f"DEAD-{node_name[0]}{node_name[-1]}"
    workdir = os.getcwd()
    node_directory = os.path.join(workdir, 'log', job_name)
    all_files = glob.glob(os.path.join(node_directory, '**/*.stdout'), recursive=True)
    if all_files:
        latest_file = max(all_files, key=os.path.getctime)
    else:
        latest_file = None
    return latest_file


def get_end_msg(fname):
    with open(fname, "r") as f:
        end_msg = f.readlines()[-1]
    return end_msg
