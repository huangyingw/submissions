#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    100.same-tree.28173106.Runtime-Error.leetcode.java \
    -t '[1,2]\n[1,null,2]'
