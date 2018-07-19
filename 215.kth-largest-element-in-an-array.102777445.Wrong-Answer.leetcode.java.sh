#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    215.kth-largest-element-in-an-array.102777445.Wrong-Answer.leetcode.java \
    -t '[2,1]\n2'
