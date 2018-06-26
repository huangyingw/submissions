#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    134.gas-station.156679993.Wrong-Answer.leetcode.py \
    -t '[3,3,4]\n[3,4,4]'
