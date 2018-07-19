#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    121.best-time-to-buy-and-sell-stock.152528888.Runtime-Error.leetcode.java \
    -t '[]'
