#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    173.binary-search-tree-iterator.155796294.Time-Limit-Exceeded.leetcode.java \
    -t '[1,null,2]'
