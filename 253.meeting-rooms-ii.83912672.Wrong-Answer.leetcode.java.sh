#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    253.meeting-rooms-ii.83912672.Wrong-Answer.leetcode.java \
    -t '[[5,8],[6,8]]'
