import subprocess


def run_script(path: str) -> None:
    assert isinstance(path, str)
    subprocess.call(path)
