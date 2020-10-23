from srv.base_commands.base_commands import run_script

from srv.checkers.constants import LINT, CHECK_SCRIPTS_PATHS, PRE_PUSH
from srv.git_hooks.git_hooks_installer import GitHooksInstaller


def init() -> None:
    GitHooksInstaller().install()


def lint() -> None:
    run_script(CHECK_SCRIPTS_PATHS[LINT])


def pre_push() -> None:
    run_script(CHECK_SCRIPTS_PATHS[PRE_PUSH])
