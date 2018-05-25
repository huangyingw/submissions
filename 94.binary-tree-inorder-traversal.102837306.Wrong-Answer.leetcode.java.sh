#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    94.binary-tree-inorder-traversal.102837306.Wrong-Answer.leetcode.java \
    -t '[]'
