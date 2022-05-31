#!/usr/bin/env python


import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff between two files with type: JSON/YML/YAML')

    parser.add_argument(
        'first_file',
        type=str,
        metavar='first_file')

    parser.add_argument(
        'second_file',
        type=str,
        metavar='second_file')

    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set output format: STYLISH (as default) | PLAIN | JSON')

    return parser.parse_args()
