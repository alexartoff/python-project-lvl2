#!/usr/bin/env python


import os
from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.plain import make_plain_format
from gendiff.formatters.json import make_json_format


FORMATTERS_FOLDER = 'formatters'
FORMATTERS = {"plain": make_plain_format,
              "json": make_json_format,
              "stylish": make_stylish_format}


def format(tree, format_name):
    if is_formatter_exist(format_name):
        return FORMATTERS[format_name](tree)
    return "Not allowed format! use: 'stylish' | 'plain' | 'json'"


def is_formatter_exist(name):
    path_to_module = os.path.dirname(__file__)
    formatters_list = os.listdir(os.path.join(path_to_module,
                                              FORMATTERS_FOLDER))
    if '__init__.py' in formatters_list:
        formatters_list.remove('__init__.py')
    formatters_name_list = [item[:-3] for item in formatters_list]
    if name in formatters_name_list:
        return True
    return False
