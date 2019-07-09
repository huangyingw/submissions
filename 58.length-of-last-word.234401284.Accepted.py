
class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s.split() else len(s.split()[-1])
