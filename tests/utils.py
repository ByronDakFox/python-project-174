from pathlib import Path


FIXTURES_PATH = Path(__file__).parent / "fixtures"


def get_fixture_path(filename):
    return FIXTURES_PATH / filename


def read_file(filename):
    return (FIXTURES_PATH / filename).read_text().strip()