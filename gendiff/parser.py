import json
import yaml
import os


def parse_file(filepath):
    _, ext = os.path.splitext(filepath)

    with open(filepath) as f:
        if ext == ".json":
            return json.load(f)
        if ext in (".yml", ".yaml"):
            return yaml.safe_load(f)

    raise ValueError(f"Unsupported file format: {ext}")
