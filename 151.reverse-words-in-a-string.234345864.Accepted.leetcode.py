class Solution(object):
    def reverseWords(self, s):
        ss = " ".join(s.split()[::-1])
        return ss
