#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    239.sliding-window-maximum.87699763.Wrong-Answer.leetcode.java \
    -t '[1,-1]\n1'
