#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    15.3sum.102349283.Wrong-Answer.leetcode.java \
    -t '[-2,0,0,2,2]'
