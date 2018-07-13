#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    171.excel-sheet-column-number.31726086.Wrong-Answer.leetcode.java \
    -t '"AB"'
