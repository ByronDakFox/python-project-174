from gendiff.parser import parse_file


def generate_diff(file1, file2):
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = ["{"]

    for key in keys:
        if key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            lines.append(f"  + {key}: {data2[key]}")
        else:
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {data1[key]}")
            else:
                lines.append(f"  - {key}: {data1[key]}")
                lines.append(f"  + {key}: {data2[key]}")

    lines.append("}")
    return "\n".join(lines)