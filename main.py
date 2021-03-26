# coding: utf-8

from cli import parse_args


HELLO_MSG = \
"""
Hello master !
Debug in progress ...
"""


def main():
    print(HELLO_MSG)
    args = parse_args()



if __name__ == '__main__':
    main()
