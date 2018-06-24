class Solution(object):
    def isPalindrome(self, s):
        if s == '':
            return True
        s = s.lower()
        start = 0
        end = len(s) - 1
        while (start < end):
            while start < end and not 'a' <= s[start] <= 'z':
                start += 1
            while start < end and not 'a' <= s[end] <= 'z':
                end -= 1
            if start < end and s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
