#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    83.remove-duplicates-from-sorted-list.81175341.Runtime-Error.leetcode.java \
    -t '[]'
