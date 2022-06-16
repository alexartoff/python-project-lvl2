#!/usr/bin/env python


from gendiff.parser import parse
from gendiff.tree import build
from gendiff.formatter import format
import os


def generate_diff(file_one, file_two, selected_format='stylish'):
    if is_allowed_type(file_one, file_two):
        with open(file_one, 'r') as data:
            dict_one = parse(data, get_file_type(file_one))
        with open(file_two, 'r') as data:
            dict_two = parse(data, get_file_type(file_two))
        diff = build(dict_one, dict_two)
        return format(diff, selected_format)
    raise ValueError("Not allowed file type! use: 'json' | 'yml' | 'yaml'")


def get_file_type(file_path):
    return str(os.path.split(file_path)[1]).split('.')[-1]


def is_allowed_type(file_one, file_two):
    allowed_types = ["json", "yml", "yaml"]
    type_one, type_two = get_file_type(file_one), get_file_type(file_two)
    if type_one in allowed_types and type_two in allowed_types:
        return True
    return False
