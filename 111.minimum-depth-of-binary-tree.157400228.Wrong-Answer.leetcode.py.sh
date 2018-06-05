#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    111.minimum-depth-of-binary-tree.157400228.Wrong-Answer.leetcode.py \
    -t '[1,2]'
