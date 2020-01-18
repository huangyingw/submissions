class Solution:
    def lengthOfLastWord(self, s):
        return 0 if not s.split() else len(s.split()[-1])
