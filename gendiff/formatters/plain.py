def format_plain(diff, parent=''):
    lines = []

    for node in diff:
        name = f"{parent}{node['key']}"
        node_type = node['type']

        if node_type == 'nested':
            lines.append(format_plain(node['children'], f"{name}."))
        elif node_type == 'added':
            lines.append(
                f"Property '{name}' was added with value: {format_value(node['value'])}"
            )
        elif node_type == 'removed':
            lines.append(
                f"Property '{name}' was removed"
            )
        elif node_type == 'changed':
            lines.append(
                f"Property '{name}' was updated. "
                f"From {format_value(node['old_value'])} "
                f"to {format_value(node['new_value'])}"
            )

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
