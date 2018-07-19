#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    252.meeting-rooms.72376313.Runtime-Error.leetcode.java \
    -t '[]'
