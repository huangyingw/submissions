#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    130.surrounded-regions.84012801.Runtime-Error.leetcode.java \
    -t '[]'
