# coding: utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Debug script to detect dead nodes")

    args = parser.parse_args()
    return args
