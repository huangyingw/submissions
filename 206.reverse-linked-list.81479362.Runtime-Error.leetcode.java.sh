#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    206.reverse-linked-list.81479362.Runtime-Error.leetcode.java \
    -t '[]'
