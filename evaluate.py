# coding: utf-8

import os
import datetime
import glob

from dispatch import NODE_LIST
from run.torch_net import END_MSG




def is_dead(node_name):
    end_msg = None # TODO
    return end_msg == END_MSG



def newest_out_file(node_name):
    job_name = f"DEAD-{node_name[0]}{node_name[-1]}"
    workdir = os.getcwd()
    node_directory = os.path.join(workdir, 'log', job_name)
    all_files = glob.glob('*.stdout', reccursive=true)
    print(all_files)
