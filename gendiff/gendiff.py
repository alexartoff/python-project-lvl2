#!/usr/bin/env python


from gendiff.parser import files_parser
from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.plain import make_plain_format
from gendiff.formatters.json import make_json_format
import os


def generate_diff(file_one, file_two, format='stylish'):
    file_one_path = get_file_path(file_one)
    file_two_path = get_file_path(file_two)
    print(file_one_path, file_two_path)
    dict_one, dict_two = files_parser(file_one_path, file_two_path)
    diff = calc_diff(dict_one, dict_two)
    if format == 'plain':
        diff_formated = make_plain_format(diff)
    elif format == 'json':
        diff_formated = make_json_format(diff)
    else:
        diff_formated = make_stylish_format(diff)
    return diff_formated


def get_file_path(file_name):
    return f"{os.getcwd()}/gendiff/tests/fixtures/{file_name}"


def calc_diff(dct_one, dct_two):
    res_dict = {}
    keys_list = make_sorted_list_from_sets(dct_one, dct_two)
    for key in keys_list:
        res_dict[key] = get_status_and_value_by_key(dct_one, dct_two, key)
    # print(f'{"*"*40}\n', res_dict, f'\n{"*"*40}')
    return res_dict


def make_sorted_list_from_sets(dct_one, dct_two):
    set_one = set(dct_one.keys())
    set_two = set(dct_two.keys())
    return sorted(set_one.union(set_two))


def get_status_and_value_by_key(dct_one, dct_two, key):
    if isinstance(dct_one.get(key), dict) and (
        isinstance(dct_two.get(key), dict)
    ):
        # item is child node
        return {'STAT': 'CHNODE',
                'CHILD': calc_diff(dct_one[key], dct_two[key])
                }
    elif dct_one.get(key) == dct_two.get(key):
        # item not changed
        return {'STAT': 'NOTCH',
                'VAL': dct_one[key]
                }
    elif key in dct_one.keys() and key not in dct_two.keys():
        # item removed
        return {'STAT': 'REMOVE',
                'VAL': dct_one[key]
                }
    elif key not in dct_one.keys() and key in dct_two.keys():
        # item added
        return {'STAT': 'ADD',
                'VAL': dct_two[key]
                }
    else:
        # item changed
        return {'STAT': 'CHANGE',
                'VAL_REM': dct_one[key],
                'VAL_ADD': dct_two[key]
                }
