class Solution:
    def isPalindrome(self, s):

        ss = ''.join(c.lower() for c in s if c.isalnum())
        return ss[::-1] == ss
