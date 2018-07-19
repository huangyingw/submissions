#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    114.flatten-binary-tree-to-linked-list.85004123.Runtime-Error.leetcode.java \
    -t '[]'
