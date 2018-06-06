#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    88.merge-sorted-array.157445188.Wrong-Answer.leetcode.py \
    -t '[2,0]\n1\n[1]\n1'
