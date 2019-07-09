_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for c in num:
            while k and result and result[-1] > c:
                result.pop()
                k -= 1
            result.append(c)
        while k:
            result.pop()
            k -= 1
        return "".join(result).lstrip("0") or "0"
