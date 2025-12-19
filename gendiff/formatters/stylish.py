INDENT = 4
SIGN_SHIFT = 2


def format_stylish(diff):
    lines = build_lines(diff, 1)
    return "{\n" + "\n".join(lines) + "\n}"


def build_lines(nodes, depth):
    result = []
    indent = " " * (INDENT * depth - SIGN_SHIFT)
    close_indent = " " * (INDENT * (depth - 1))

    for node in nodes:
        key = node["key"]
        t = node["type"]

        if t == "nested":
            result.append(
                f"{indent}  {key}: {{\n"
                + "\n".join(build_lines(node["children"], depth + 1))
                + f"\n{close_indent}  }}"
            )

        elif t == "added":
            result.append(
                f"{indent}+ {key}: {stringify(node['value'], depth)}"
            )

        elif t == "removed":
            result.append(
                f"{indent}- {key}: {stringify(node['value'], depth)}"
            )

        elif t == "unchanged":
            result.append(
                f"{indent}  {key}: {stringify(node['value'], depth)}"
            )

        elif t == "changed":
            result.append(
                f"{indent}- {key}: {stringify(node['old_value'], depth)}"
            )
            result.append(
                f"{indent}+ {key}: {stringify(node['new_value'], depth)}"
            )

    return result


def stringify(value, depth):
    if not isinstance(value, dict):
        return str(value)

    indent = " " * (INDENT * depth)
    close_indent = " " * (INDENT * (depth - 1))

    lines = [
        f"{indent}{k}: {stringify(v, depth + 1)}"
        for k, v in value.items()
    ]

    return "{\n" + "\n".join(lines) + f"\n{close_indent}}}"
