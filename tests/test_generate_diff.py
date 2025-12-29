import json
from gendiff import generate_diff
from utils import get_fixture_path, read_file



def test_nested_json():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected = read_file("expected_stylish.txt")

    assert generate_diff(file1, file2) == expected


def test_nested_yaml():
    file1 = get_fixture_path("file1.yml")
    file2 = get_fixture_path("file2.yml")
    expected = read_file("expected_stylish.txt")

    assert generate_diff(file1, file2) == expected

def test_json_format():
    result = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
        'json'
    )

    parsed = json.loads(result)

    assert isinstance(parsed, list)
    assert parsed[0]['key'] == 'common'
    assert parsed[0]['type'] == 'nested'

