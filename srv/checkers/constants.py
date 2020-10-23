import os
from pathlib import Path

CURRENT_PATH = Path(os.path.dirname(os.path.abspath(__file__)))

LINT = 'lint'
PRE_PUSH = 'pre_push'

CHECK_SCRIPTS_PATHS = {
    'lint': f'{CURRENT_PATH}/pre_commit.sh',
    'pre_push': f'{CURRENT_PATH}/pre_push.sh',
}
