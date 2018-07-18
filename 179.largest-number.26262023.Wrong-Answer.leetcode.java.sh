#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    179.largest-number.26262023.Wrong-Answer.leetcode.java \
    -t '[0,0]'
