def make_plain_format(tree):
    depth = 0
    output_list = []

    for child in tree['children']:
        if "children" in child.keys():
            begin_str = ''
        else:
            begin_str = f'Property \'{child["key"]}'
        inlist = (f'{begin_str}'
                  f'{make_formated_string(child, depth, child["key"])}')
        output_list.append(inlist)
    return '\n'.join(output_list)


def make_formated_string(node, depth, key):
    accum_list = []
    child_keys = key

    if node['type'] == 'child_node':
        for child in node['children']:
            begin_str = ''
            if child['type'] == 'child_node':
                child_keys += f'.{child["key"]}'
            elif child['type'] in ['changed', 'added', 'removed']:
                begin_str = f'Property \'{key}.{child["key"]}'
            else:
                continue
            inlist = (f'{begin_str}'
                      f'{make_formated_string(child, depth + 1, child_keys)}')
            accum_list.append(inlist)
    else:
        accum_list.append(make_suffix_string(node))
    return '\n'.join(accum_list)


def make_suffix_string(node):
    node_status = node['type']
    suffix_dict = {'added': '\' was added with value: ',
                   'removed': '\' was removed',
                   'changed': '\' was updated. '
                   }
    if node_status == 'changed':
        value_rem = node['value_rem']
        value_add = node['value_add']
        return (f'{suffix_dict[node_status]}'
                f'From {normalize_values(value_rem)} '
                f'to {normalize_values(value_add)}')
    if node_status == 'added':
        node_value = node['value']
        return (f'{suffix_dict[node_status]}'
                f'{normalize_values(node_value)}')
    if node_status == 'removed':
        return suffix_dict[node_status]


def normalize_values(value):
    norm = {'True': 'true', 'False': 'false', 'None': 'null'}
    for key, norm_val in norm.items():
        if str(value) == key:
            value = norm_val
            return str(value)
    if isinstance(value, dict):
        return convert_dict_to_formated_str(value)
    elif isinstance(value, int):
        return f'{str(value)}'
    return f'\'{str(value)}\''


def convert_dict_to_formated_str(dct):
    accum_list = []
    if isinstance(dct, dict):
        accum_list.append('[complex value]')
    return '\n'.join(accum_list)
