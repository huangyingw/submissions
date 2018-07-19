#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    125.valid-palindrome.153382240.Wrong-Answer.leetcode.py \
    -t '"0P"'
