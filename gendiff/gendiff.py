#!/usr/bin/env python


from gendiff.parser import parse
from gendiff.tree import build
from gendiff.formatter import format
import os


def generate_diff(file_one, file_two, selected_format='stylish'):
    diff = build(get_data(file_one), get_data(file_two))
    return format(diff, selected_format)


def get_data(file_path):
    with open(file_path, 'r') as data:
        return parse(data, get_file_type(file_path))


def get_file_type(file_path):
    return str(os.path.split(file_path)[1]).split('.')[-1]
