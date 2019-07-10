_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def judgeCircle(self, moves):

        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
