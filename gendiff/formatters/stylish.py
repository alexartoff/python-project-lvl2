def make_stylish_format(tree):
    return iter_(tree)


def iter_(node, depth=0):
    children = node.get('children')
    indent = build_indent(depth)
    formatted_value = to_str(node.get('value'), depth)
    formatted_value_add = to_str(node.get('value_add'), depth)
    formatted_value_rem = to_str(node.get('value_rem'), depth)

    if node['type'] == 'root_node':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node['type'] == 'child_node':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{indent}  {node["key"]}: {{\n{result}\n  {indent}}}'

    if node['type'] in ['not_changed', 'added', 'removed']:
        indent_for = {'not_changed': '  ', 'added': '+ ', 'removed': '- '}
        return (f'{indent}{indent_for[node["type"]]}'
                f'{node["key"]}: {formatted_value}')

    if node['type'] == 'changed':
        line_rem = f'{indent}- {node["key"]}: {formatted_value_rem}\n'
        line_add = f'{indent}+ {node["key"]}: {formatted_value_add}'
        return line_rem + line_add


def build_indent(depth):
    return f'{" " * (4 * depth - 2)}'


def to_str(data, depth):
    if isinstance(data, dict):
        indent = build_indent(depth) + (' ' * 6)
        lines = [(f'{indent}{key}: {to_str(val, depth + 1)}'
                  f'') for key, val in data.items()]
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {build_indent(depth)}}}'

    if isinstance(data, bool):
        if data:
            return 'true'
        return 'false'

    if data is None:
        return 'null'

    return str(data)
