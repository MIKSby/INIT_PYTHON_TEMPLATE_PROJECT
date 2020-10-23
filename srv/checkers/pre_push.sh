#!/bin/bash

echo ">>> $(basename "${BASH_SOURCE[0]}")"

set -o errexit
set -o pipefail
set -o nounset

# INIT WORKING DIR
# ======================================================================================================
cd "$(dirname "${BASH_SOURCE[0]}")"
FILE_DIR=$(pwd)
cd ../../
CWD="$(pwd)"

# INIT COLOR HIGHLIGHTING
# ===================================================

RED='\033[0;31m'
RED_BG='\e[41m'
BLACK='\e[1;30m'
CYAN='\e[36m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m'

process_counter=0
function start_section() {
  process_counter=$((process_counter + 1))
  echo -e "${BLUE}[STEP ${process_counter} : ${1}]${NC}"
}
function end_section() {
  COUNT_OF_ERRORS=$1
  if ((${COUNT_OF_ERRORS} > 0)); then
    echo -e "\n${RED_BG}${BLACK}  FAILED  ${NC}   ${1} errors found\n"
    exit 1
  fi
  echo -e "${GREEN}>> DONE without errors${NC}\n"
}

# SEARCH ALL PY FILES
# ===================================================

PY_FILES=$(find . -type f -name "*.py" ! -path './.*' -not -path "**/migrations/*" -not -path "./manage.py" -not -path "**/settings.py" -not -path "**/apps_config/*")
echo "$PY_FILES"

# RUN PRE-PUSH LINTING:
# 1. safety
# 2. bandit
# ===================================================

start_section "CHECK VULNERABILITIES OF PACKAGES : SAFETY"
cd "${CWD}"
#safety check --ignore 37261
safety check
end_section 0

start_section "CHECK SECURITY : BANDIT"
cd "${CWD}"
bandit -c .bandit.yml -r -ll "${CWD}"
end_section 0

# END
# ===================================================

echo ">>> $(basename "${BASH_SOURCE[0]}") DONE"
