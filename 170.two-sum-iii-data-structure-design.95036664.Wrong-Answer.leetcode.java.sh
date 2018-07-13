#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    170.two-sum-iii-data-structure-design.95036664.Wrong-Answer.leetcode.java \
    -t '["TwoSum","add","find"]\n[[],[0],[0]]'
