#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l
leetcode test \
    139.word-break.155001683.Wrong-Answer.leetcode.java \
    -t '"aaaaaaa"\n["aaaa","aaa"]'
