#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    102.binary-tree-level-order-traversal.156057375.Runtime-Error.leetcode.py \
    -t '[]'
