#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    156.binary-tree-upside-down.32896997.Wrong-Answer.leetcode.java \
    -t '[1,2]'
