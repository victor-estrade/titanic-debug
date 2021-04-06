# coding: utf-8

import os
import datetime
import glob

from dispatch import NODE_LIST
from run.common import END_MSG



def evaluate_all():
    for node_name in NODE_LIST:
        if is_dead(node_name):
            print(f"[DEAD] {node_name}")
        else:
            print(f"[ALIVE] {node_name}")


def is_dead(node_name):
    fname = newest_out_file(node_name)
    end_msg = get_end_msg(fname)
    return end_msg == END_MSG



def newest_out_file(node_name):
    job_name = f"DEAD-{node_name[0]}{node_name[-1]}"
    workdir = os.getcwd()
    node_directory = os.path.join(workdir, 'log', job_name)
    all_files = glob.glob('*.stdout', reccursive=True)
    print(all_files)


def get_end_msg(fname):
    return 'TODO'
