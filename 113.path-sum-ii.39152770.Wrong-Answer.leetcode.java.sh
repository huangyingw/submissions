#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    113.path-sum-ii.39152770.Wrong-Answer.leetcode.java \
    -t '[-2,null,-3]\n-5'
