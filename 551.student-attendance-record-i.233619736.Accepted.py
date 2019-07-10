_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def checkRecord(self, s):

        return s.count("A") < 2 and "LLL" not in s
