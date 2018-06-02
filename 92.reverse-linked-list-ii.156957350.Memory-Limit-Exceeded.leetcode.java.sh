#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    92.reverse-linked-list-ii.156957350.Memory-Limit-Exceeded.leetcode.java \
    -t '[3,5]\n1\n1'
