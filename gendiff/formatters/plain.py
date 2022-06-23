def make_plain_format(tree):
    return iter_(tree)


def iter_(node, key_depth=""):
    children = node.get('children')
    keys_chain = key_depth + str(node.get("key"))
    formatted_value = to_str(node.get('value'))
    formatted_value_add = to_str(node.get('value_add'))
    formatted_value_rem = to_str(node.get('value_rem'))

    if node['type'] == 'root_node':
        lines = map(lambda child: iter_(child, key_depth), children)
        result = ''.join(lines)
        return f'{result[1:]}'

    if node['type'] == 'child_node':
        lines = map(lambda child: iter_(child, f"{keys_chain}."), children)
        result = ''.join(filter(bool, lines))
        return f'{result}'

    if node['type'] == 'added':
        return (f'\nProperty \'{keys_chain}\' '
                f'was added with value: {formatted_value}')

    if node['type'] == 'removed':
        return f'\nProperty \'{keys_chain}\' was removed'

    if node['type'] == 'changed':
        return (f'\nProperty \'{keys_chain}\' was updated. '
                f'From {formatted_value_rem} to {formatted_value_add}')


def to_str(data):
    if isinstance(data, dict):
        return '[complex value]'

    if isinstance(data, bool):
        if data:
            return 'true'
        return 'false'

    if data is None:
        return 'null'

    return f"'{str(data)}'"
