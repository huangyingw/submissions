#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    75.sort-colors.102560593.Wrong-Answer.leetcode.java \
    -t '[2,0,1]'
