#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    97.interleaving-string.8308656.Wrong-Answer.leetcode.java \
    -t '""\n""\n""'
