from gendiff import generate_diff
from utils import get_fixture_path, read_file


def test_plain_format():
    file1 = get_fixture_path("file1.json")
    file2 = get_fixture_path("file2.json")
    expected = read_file("expected_plain.txt")

    assert generate_diff(file1, file2, 'plain') == expected
