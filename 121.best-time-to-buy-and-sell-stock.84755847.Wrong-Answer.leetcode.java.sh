#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    121.best-time-to-buy-and-sell-stock.84755847.Wrong-Answer.leetcode.java \
    -t '[7,6,4,3,1]'
