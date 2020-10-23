import os
import shutil
import stat
from pathlib import Path
from typing import List

FILENAMES_TO_COPY_IN_GIT_HOOKS_DIR: List[str] = [
    'pre-commit',
    'pre-push',
]


class GitHooksInstaller:
    def __init__(self) -> None:
        self.project_hooks_path = Path(os.path.dirname(os.path.abspath(__file__)))
        self.git_hooks_path = Path(f'{self.project_hooks_path.parents[1]}/.git/hooks')

    def check_if_already_installed(self) -> bool:
        return all([Path(f'{self.git_hooks_path}/{fn}').is_file() and not Path(f'{self.git_hooks_path}/{fn}.sample').is_file() for fn in FILENAMES_TO_COPY_IN_GIT_HOOKS_DIR])

    def install(self) -> None:
        assert all(map(lambda x: type(x) is str, FILENAMES_TO_COPY_IN_GIT_HOOKS_DIR))

        if self.check_if_already_installed():
            print('hooks was already installed. skipping')
            return None

        for source, destination in ((f'{self.project_hooks_path}/hooks/{fn}', f'{self.git_hooks_path}/{fn}') for fn in FILENAMES_TO_COPY_IN_GIT_HOOKS_DIR):
            shutil.copyfile(source, destination)
            try:
                os.remove(f'{destination}.sample')
            except FileNotFoundError:
                pass
        for hook_file in FILENAMES_TO_COPY_IN_GIT_HOOKS_DIR:
            file = f'{self.git_hooks_path}/{hook_file}'
            st = os.stat(file)
            os.chmod(file, st.st_mode | stat.S_IEXEC)

        print('hooks is installed!')


if __name__ == '__main__':
    GitHooksInstaller().install()
