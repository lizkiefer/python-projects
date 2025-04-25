#!/bin/bash

# v2.0.1
# run the command below to see if you have the correct pinned version of pylint
# pylint --version
# pylint 2.17.7
# astroid 2.15.8
# Python 3.11.7 (main, Jan 16 2024, 14:42:22) [Clang 14.0.0 (clang-1400.0.29.202)]

# run the command below to see if you have the correct pinned version of flake8
# flake8 --version
# 6.1.0 (mccabe: 0.7.0, pycodestyle: 2.11.1, pyflakes: 3.1.0) CPython 3.11.7 on Darwin


if [ $# -eq 0 ]
      then
              echo "No directory supplied, eg: bash $0 assignment2"
                  exit
fi

ENFORCED_FILES="
$1
"

# Disable R0914: Too many local variables
# Disable E0401: Flask CORS ext
# would have been caught by pylint.
# Disable C0121: Comparison to True should be just 'expr'
# assigment 3 on...
# Disable R0801: Similar lines in 2 files
# Disable R1705: Unnecessary "else" after "return"
# Disable R1732: Consider using 'with' for resource-allocating operations (consider-using-with)"
MAX_LINE_LEN="--max-line-length=120"

echo "Running pylint..."
pylint  \
    --extension-pkg-whitelist=math \
    --disable=R0914,E0401,C0121,R0801,R1705,R1732 $MAX_LINE_LEN \
    --msg-template='{abspath}:{line:3d}: {obj}: {msg_id}:{msg}' \
    $ENFORCED_FILES


if [ $? -ne 0 ]; then
      echo "pylint failed, stopping script."
        exit 1
fi

# assignment 3 on...
# Disable: E712 comparison to True should be 'if cond is True:' or 'if cond:'
# Diaable:  W504 line break after binary operator
echo -e "\n\nRunning flake8..."
flake8  --max-complexity 12 --benchmark $MAX_LINE_LEN --ignore=R0914,E712,W504 $ENFORCED_FILES


if [ $? -ne 0 ]; then
      echo "flake8 failed, stopping script."
        exit 1
fi

echo -e "\n\n*****Nice work! All lints passed successfully.****"
