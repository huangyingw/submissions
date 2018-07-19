#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    153.find-minimum-in-rotated-sorted-array.156689442.Wrong-Answer.leetcode.java \
    -t '[1,2,3]'
