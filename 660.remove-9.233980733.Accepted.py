_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def newInteger(self, n):

        result = []
        while n:
            result.append(str(n % 9))
            n //= 9
        return int("".join(result[::-1]))
