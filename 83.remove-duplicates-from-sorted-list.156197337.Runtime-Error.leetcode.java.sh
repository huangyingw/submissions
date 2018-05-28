#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    83.remove-duplicates-from-sorted-list.156197337.Runtime-Error.leetcode.java \
    -t '[1,1,2,3,3]'
