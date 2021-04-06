# coding: utf-8

from cli import parse_args

from dispatch import launch_on_all_nodes

HELLO_MSG = \
"""
Hello master !
Debug in progress ...
"""


def main():
    print(HELLO_MSG)
    args = parse_args()
    launch_on_all_nodes()




if __name__ == '__main__':
    main()
