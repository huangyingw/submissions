#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    97.interleaving-string.160349412.Wrong-Answer.leetcode.py \
    -t '"ab"\n"bc"\n"bbac"'
