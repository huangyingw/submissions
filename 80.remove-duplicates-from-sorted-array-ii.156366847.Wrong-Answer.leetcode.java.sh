#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    80.remove-duplicates-from-sorted-array-ii.156366847.Wrong-Answer.leetcode.java \
    -t '[1,2,2]'
leetcode test \
    80.remove-duplicates-from-sorted-array-ii.82226273.Accepted.leetcode.java \
    -t '[1,2,2]'
