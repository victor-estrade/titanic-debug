# coding: utf-8

from cli import parse_args

from dispatch import launch_on_all_nodes
from evaluate import evaluate_all

HELLO_MSG = \
"""
Hello master !
Debug in progress ...
"""


def main():
    print(HELLO_MSG)
    args = parse_args()
    if args.action == "run"
        launch_on_all_nodes()
    elif args.action == "eval":
        evaluate_all()




if __name__ == '__main__':
    main()
