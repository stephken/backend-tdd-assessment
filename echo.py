#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "???"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true', help='convert text to titlecase')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)

    if args.lower:
        print(args.text.lower())
    if args.upper:
        print(args.text.upper())
    if args.title:
        print(args.text.title())            
    else:
        print(args.text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
