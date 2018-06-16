#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    112.path-sum.152690218.Wrong-Answer.leetcode.java \
    -t '[1,2]\n1'
