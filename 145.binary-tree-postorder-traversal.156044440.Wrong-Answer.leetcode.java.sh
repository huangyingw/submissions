#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    145.binary-tree-postorder-traversal.156044440.Wrong-Answer.leetcode.java \
    -t '[]'
