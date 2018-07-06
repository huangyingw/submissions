#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    154.find-minimum-in-rotated-sorted-array-ii.32631364.Runtime-Error.leetcode.java \
    -t '[1,1,1]'
leetcode test \
    154.find-minimum-in-rotated-sorted-array-ii.32631364.Runtime-Error.leetcode.java \
    -t '[1]'
