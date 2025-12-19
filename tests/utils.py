from pathlib import Path

FIXTURE_PATH = Path(__file__).parent / "fixture"

def get_fixture_path(filename):
    return FIXTURE_PATH / filename

def read_file(filename):
    return Path(FIXTURE_PATH / filename).read_text().strip()
