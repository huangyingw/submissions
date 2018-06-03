#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    97.interleaving-string.84028115.Runtime-Error.leetcode.java \
    -t '"a"\n"b"\n"a"'
