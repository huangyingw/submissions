_author_ = 'jake'
_project_ = 'leetcode'






from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):

        return Counter(s) == Counter(t)
