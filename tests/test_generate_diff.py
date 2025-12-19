from gendiff import generate_diff
from utils import get_fixture_path, read_file

def test_nested_json_stylish():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected = get_fixture_path("expected_stylish.txt")