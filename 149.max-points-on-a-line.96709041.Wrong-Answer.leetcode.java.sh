#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    149.max-points-on-a-line.96709041.Wrong-Answer.leetcode.java \
    -t '[[0,0],[1,65536],[65536,0]]'
