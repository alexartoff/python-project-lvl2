#!/usr/bin/env python


def calc_diff(data_one, data_two):
    result = []
    keys = data_one.keys() | data_two.keys()
    sorted_keys_list = sorted(keys)

    for key in sorted_keys_list:
        if isinstance(data_one.get(key), dict) and (
            isinstance(data_two.get(key), dict)
        ):
            result.append({
                'key': key,
                'type': 'child_node',
                'children': calc_diff(data_one[key], data_two[key])
            })
        elif data_one.get(key) == data_two.get(key):
            result.append({
                'key': key,
                'type': 'not_changed',
                'value': data_one[key]
            })
        elif key not in data_two:
            result.append({
                'key': key,
                'type': 'removed',
                'value': data_one[key]
            })
        elif key not in data_one:
            result.append({
                'key': key,
                'type': 'added',
                'value': data_two[key]
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'value_rem': data_one[key],
                'value_add': data_two[key]
            })
    return result


def build(data_one, data_two):
    return {
        'type': 'root_node',
        'children': calc_diff(data_one, data_two)
    }
