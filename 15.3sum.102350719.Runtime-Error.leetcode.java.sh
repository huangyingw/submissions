#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    15.3sum.102350719.Runtime-Error.leetcode.java \
    -t '[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4]'
