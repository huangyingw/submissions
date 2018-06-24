#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    128.longest-consecutive-sequence.94681119.Wrong-Answer.leetcode.java \
    -t '[]'
