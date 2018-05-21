#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode test \
    90.subsets-ii.102868422.Wrong-Answer.leetcode.java \
    -t '[4,4,4,1,4]'
