#!/usr/bin/env python


from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.plain import make_plain_format
from gendiff.formatters.json import make_json_format


def format(tree, format_name):
    if format_name == "plain":
        return make_plain_format(tree)
    if format_name == "json":
        return make_json_format(tree)
    if format_name == "stylish":
        return make_stylish_format(tree)
    raise ValueError(f"Not supported format - '{format_name}'")
