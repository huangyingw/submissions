#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode test \
    ./submissions/139.word-break.90221939.Wrong-Answer.leetcode.java \
    -t '"aaaaaaa"\n["aaaa","aaa"]'

