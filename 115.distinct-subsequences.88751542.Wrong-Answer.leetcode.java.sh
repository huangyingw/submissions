#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    115.distinct-subsequences.88751542.Wrong-Answer.leetcode.java \
    -t '"babgbag"\n"bag"'
