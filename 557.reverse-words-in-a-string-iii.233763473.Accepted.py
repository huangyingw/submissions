_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def reverseWords(self, s):

        return " ".join([w[::-1] for w in s.split(" ")])
