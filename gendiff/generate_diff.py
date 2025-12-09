import json


def parse_file(filepath):
    with open(filepath) as f:
        return json.load(f)


def generate_diff(file1, file2):
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = ["{"]

    for key in keys:
        if key not in data2:
            # Fue eliminado
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            # Fue agregado
            lines.append(f"  + {key}: {data2[key]}")
        else:
            # Está en ambos
            if data1[key] == data2[key]:
                lines.append(f"    {key}: {data1[key]}")
            else:
                # Cambió de valor
                lines.append(f"  - {key}: {data1[key]}")
                lines.append(f"  + {key}: {data2[key]}")

    lines.append("}")
    return "\n".join(lines)
