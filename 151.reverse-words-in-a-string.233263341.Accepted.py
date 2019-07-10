_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def reverseWords(self, s):

        words = s.split()
        return " ".join(words[::-1])
