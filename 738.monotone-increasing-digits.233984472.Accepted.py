_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = [int(c) for c in str(N)]
        i = 0
        while i + 1 < len(s):
            if s[i + 1] < s[i]:
                while i > 0 and s[i] - 1 < s[i - 1]:
                    i -= 1
                s[i] -= 1
                s[i + 1:] = [9] * (len(s) - i - 1)
                result = 0
                for val in s:
                    result = result * 10 + val
                return result
            else:
                i += 1
        return N
