#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    17.letter-combinations-of-a-phone-number.34003011.Wrong-Answer.leetcode.java \
    -t '""'
