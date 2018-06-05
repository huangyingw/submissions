#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    88.merge-sorted-array.102702866.Runtime-Error.leetcode.java \
    -t '[0]\n0\n[1]\n1'
