def make_plain_format(dct):
    output_list = []
    depth = 0
    for key in dct.keys():
        parent = key
        inner_dict = dct[key]
        begin_str = ''
        if inner_dict["STAT"] != "CHNODE":
            begin_str = f'Property \'{parent}'
        inlist = (f'{begin_str}'
                  f'{make_formated_string(dct[key], depth, key, parent)}')
        output_list.append(inlist)
    return '\n'.join(output_list)


def make_formated_string(node, depth, key, parent):
    accum_list = []
    keys = parent

    if node['STAT'] == 'CHNODE':
        for key, val in node['CHILD'].items():
            begin_str = ''
            if val['STAT'] == 'CHNODE':
                keys += f'.{key}'
                # print(f'{"    "*depth}CHL {parent} {keys} {depth}')
            elif val['STAT'] in ['CHANGE', 'ADD', 'REMOVE']:
                begin_str = f'Property \'{parent}.{key}'
                # print(f'{"    "*depth}VAL {parent} {key} {depth} {val}')
            else:
                continue
            inlist = (f'{begin_str}'
                      f'{make_formated_string(val, depth + 1, key, keys)}')
            accum_list.append(inlist)
    else:
        accum_list.append(make_suffix_string(node))
    return '\n'.join(accum_list)


def make_suffix_string(node):
    node_status = node['STAT']
    suffix_dict = {'ADD': '\' was added with value: ',
                   'REMOVE': '\' was removed',
                   'CHANGE': '\' was updated. '
                   }
    if node_status == 'CHANGE':
        value_rem = node['VAL_REM']
        value_add = node['VAL_ADD']
        inlist = (f'{suffix_dict[node_status]}'
                  f'From {normalize_values(value_rem)} '
                  f'to {normalize_values(value_add)}')
    elif node_status == 'ADD':
        node_value = node['VAL']
        inlist = (f'{suffix_dict[node_status]}'
                  f'{normalize_values(node_value)}')
    elif node_status == 'REMOVE':
        inlist = suffix_dict[node_status]
    return inlist


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
