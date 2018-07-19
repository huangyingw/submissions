#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    169.majority-element.156784036.Wrong-Answer.leetcode.java \
    -t '[2,2,1,1,1,2,2]'
