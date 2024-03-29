class Solution:
    def longestPalindrome(self, s):
        result = ''
        for i in range(len(s)):
            odd = self.getPalindrome(i, i, s)
            if len(result) < len(odd):
                result = odd
            even = self.getPalindrome(i, i + 1, s)
            if len(result) < len(even):
                result = even
        return result

    def getPalindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l:r - 1]
