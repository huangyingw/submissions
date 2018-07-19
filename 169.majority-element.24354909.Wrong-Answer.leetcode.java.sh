#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    169.majority-element.24354909.Wrong-Answer.leetcode.java \
    -t '[3,3,4]'
