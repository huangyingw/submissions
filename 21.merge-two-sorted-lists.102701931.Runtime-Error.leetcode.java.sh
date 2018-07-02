#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    21.merge-two-sorted-lists.102701931.Runtime-Error.leetcode.java \
    -t '[1]\n[2]'
