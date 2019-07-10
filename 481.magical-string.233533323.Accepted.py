_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def magicalString(self, n):

        if n == 0:
            return 0
        i = 2
        s = [1, 2, 2]
        ones = 1
        while len(s) < n:
            digit = s[-1] ^ 3
            s.append(digit)
            if s[i] == 2:
                s.append(digit)
            if digit == 1:
                ones += s[i]
            i += 1
        if len(s) > n and s[-1] == 1:
            ones -= 1
        return ones
