#!/usr/bin/env python


def calc_diff(dct_one, dct_two):
    res_dict = {}
    keys_list = make_sorted_list_from_sets(dct_one, dct_two)
    for key in keys_list:
        res_dict[key] = get_status_and_value_by_key(dct_one, dct_two, key)
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
