OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
OFFSET = '    '
OFFSET_ADD = '  + '
OFFSET_REM = '  - '


def make_stylish_format(tree):
    output_list = []
    depth = 0
    for key in tree.keys():
        if tree[key] == 'root_node':
            output_list.append(OPEN_BRACKET)
        if key == 'children':
            for child in tree['children']:
                output_list.append(make_f_string(child, depth, child['key']))
    output_list.append(CLOSE_BRACKET)
    return '\n'.join(output_list)


def make_f_string(node, depth, key):
    accum_list = []
    if node['type'] == 'child_node':
        accum_list.append(f'{OFFSET*(depth + 1)}{key}: {OPEN_BRACKET}')
        for child in node['children']:
            accum_list.append(make_f_string(child, depth + 1, child['key']))
        accum_list.append(f'{OFFSET*(depth + 1)}{CLOSE_BRACKET}')
    elif node['type'] in ['not_changed', 'added', 'removed']:
        accum_list.append(make_string_for_list(node, depth, key))
    elif node['type'] == 'changed':
        value_rem = node['value_rem']
        value_add = node['value_add']
        inlist = (f'{OFFSET*depth}{OFFSET_REM}{key}: '
                  f'{normalize_values(value_rem, depth)}\n'
                  f'{OFFSET*depth}{OFFSET_ADD}{key}: '
                  f'{normalize_values(value_add, depth)}')
        accum_list.append(inlist)
    return '\n'.join(accum_list)


def make_string_for_list(node, depth, key):
    node_status = {'added': 'ADD', 'removed': 'REM'}
    if node['type'] == 'not_changed':
        offset = ""
        depth_value = depth + 1
    else:
        offset = globals()[f"OFFSET_{node_status[node['type']]}"]
        depth_value = depth
    inlist = (f'{OFFSET*depth_value}{offset}{key}: '
              f'{normalize_values(node["value"], depth)}')
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
