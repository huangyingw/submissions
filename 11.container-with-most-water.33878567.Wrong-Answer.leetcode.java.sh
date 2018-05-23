#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    11.container-with-most-water.33878567.Wrong-Answer.leetcode.java \
    -t '[2,1]'
