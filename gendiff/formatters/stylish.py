OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
OFFSET = '    '
OFFSET_ADD = '  + '
OFFSET_REMOVE = '  - '


def make_stylish_format(dct):
    output_list = [OPEN_BRACKET]
    depth = 0
    for key in dct.keys():
        output_list.append(make_formated_string(dct[key], depth, key))
    output_list.append(CLOSE_BRACKET)
    return '\n'.join(output_list)


def make_formated_string(node, depth, key):
    accum_list = []
    if node['STAT'] == 'CHNODE':
        accum_list.append(f'{OFFSET*(depth + 1)}{key}: {OPEN_BRACKET}')
        for key, val in node['CHILD'].items():
            accum_list.append(make_formated_string(val, depth + 1, key))
        accum_list.append(f'{OFFSET*(depth + 1)}{CLOSE_BRACKET}')
    elif node['STAT'] in ['NOTCH', 'ADD', 'REMOVE']:
        accum_list.append(make_string_for_list(node, depth, key))
    elif node['STAT'] == 'CHANGE':
        value_rem = node['VAL_REM']
        value_add = node['VAL_ADD']
        inlist = (f'{OFFSET*depth}{OFFSET_REMOVE}{key}: '
                  f'{normalize_values(value_rem, depth)}\n'
                  f'{OFFSET*depth}{OFFSET_ADD}{key}: '
                  f'{normalize_values(value_add, depth)}')
        accum_list.append(inlist)
    return '\n'.join(accum_list)


def make_string_for_list(node, depth, key):
    status = node['STAT']
    value = node['VAL']
    offset = "" if status == 'NOTCH' else globals()[f"OFFSET_{status}"]
    depth_value = (depth + 1) if status == 'NOTCH' else depth
    inlist = (f'{OFFSET*depth_value}{offset}{key}: '
              f'{normalize_values(value, depth)}')
    return inlist


def normalize_values(value, depth):
    norm = {'True': 'true', 'False': 'false', 'None': 'null'}
    for key, norm_val in norm.items():
        if str(value) == key:
            value = norm_val
    if isinstance(value, dict):
        return convert_dict_to_formated_str(value, depth + 1)
    return str(value)


def convert_dict_to_formated_str(dct, depth):
    accum_list = []
    if isinstance(dct, dict):
        accum_list.append(OPEN_BRACKET)
        for key in dct.keys():
            inlist = (
                f'{OFFSET*(depth+1)}{key}: '
                f'{convert_dict_to_formated_str(dct[key], depth + 1)}')
            accum_list.append(inlist)
        accum_list.append(f'{OFFSET*depth}{CLOSE_BRACKET}')
    else:
        accum_list.append(normalize_values(dct, depth))
    return '\n'.join(accum_list)
