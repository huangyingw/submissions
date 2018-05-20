#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode test \
    239.sliding-window-maximum.88578393.Wrong-Answer.leetcode.java \
    -t '[7,2,4]\n2'
