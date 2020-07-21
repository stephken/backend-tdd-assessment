#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="transforming input text")
    parser.add_argument('text', help='text to echo')
    parser.add_argument('-l', action='store_true',
                        help='transform txt to lowercase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)

    if args.l:
        print(args.txt.lower())
    else:
        print(args.txt)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
