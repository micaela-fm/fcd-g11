from pathlib import Path


def get_project_root():
    """Return the repository root path."""
    return Path(__file__).resolve().parents[3]


def get_a3_root():
    """Return the A3 project root path."""
    return get_project_root() / "A3"


def relative_to_project(path):
    """Return a path relative to the repository root."""
    return Path(path).relative_to(get_project_root()).as_posix()
