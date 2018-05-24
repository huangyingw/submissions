#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    155.min-stack.102815421.Runtime-Error.leetcode.java \
    -t '["MinStack","push","push","push","getMin","pop","getMin"]\n[[],[0],[1],[0],[],[],[]]'
