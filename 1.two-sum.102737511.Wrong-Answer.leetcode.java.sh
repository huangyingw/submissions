#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    1.two-sum.102737511.Wrong-Answer.leetcode.java \
    -t '[3,2,4]\n6'
