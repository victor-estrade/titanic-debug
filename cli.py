# coding: utf-8
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import argparse
import json

def parse_args():
    config = read_config()

    parser = argparse.ArgumentParser(description="Debug script to detect dead nodes")

    parser.add_argument('action', help='action to do', choices=("run", "eval"))
    parser.add_argument("--gpu", type=int,
                        default=config["gpu"], help="number of gpu resquested")
    parser.add_argument("--cpu", type=int,
                        default=config["cpu"], help="number of cpu resquested")
    parser.add_argument("--memory", type=str,
                        default=config["memory"], help="amount of memory resquested")

    parser.add_argument("--docker-image", type=str,
                        default=config["docker_image"], help="docker image")
    parser.add_argument("--partition", type=str, choices=("titanic", "besteffort"),
                        default=config["partition"], help="partition on which to run the test script")
    parser.add_argument("--benchmark", type=str,
                        default=config["benchmark"], help="name of the test script module")
    parser.add_argument("--main-args", type=str,
                        default=config["main_args"], help="arguments to pass to the test script")

    args = parser.parse_args()
    return args



def read_config(fname="config.json"):
    try:
        config = _read_config(fname)
    except Exception as e:
        DEFAULT_CONFIG_FNAME = "default_config.json"
        print("[WARNING] : error with given config file name !")
        print(f"[WARNING] : Error message = {e}")
        print(f"[WARNING] : Using {DEFAULT_CONFIG_FNAME} instead")
        try:
            config = _read_config(DEFAULT_CONFIG_FNAME)
        except Exception as e:
            raise e
    return config


def _read_config(fname):
    with open(fname, "r") as file:
        config = json.load(file)
    assert_config_complete(config, fname)
    return config


def assert_config_complete(config, fname):
    assert "cpu" in config, f' "cpu" option is missing in configuration file {fname}'
    assert "memory" in config, f' "memory" option is missing in configuration file {fname}'
    assert "partition" in config, f' "partition" option is missing in configuration file {fname}'
    assert "gpu" in config, f' "gpu" option is missing in configuration file {fname}'
    assert "docker_image" in config, f' "docker_image" option is missing in configuration file {fname}'
    assert "benchmark" in config, f' "benchmark" option is missing in configuration file {fname}'
    assert "main_args" in config, f' "main_args" option is missing in configuration file {fname}'
