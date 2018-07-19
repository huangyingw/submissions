#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    165.compare-version-numbers.24610108.Wrong-Answer.leetcode.java \
    -t '"1"\n"1.1"'
