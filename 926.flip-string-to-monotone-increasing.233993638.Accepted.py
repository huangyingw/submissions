_author_ = 'jake'
_project_ = 'leetcode'













class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zeros, ones = S.count("0"), 0
        result = zeros
        for c in S:
            if c == "0":
                zeros -= 1
            else:
                ones += 1
            result = min(result, zeros + ones)
        return result
