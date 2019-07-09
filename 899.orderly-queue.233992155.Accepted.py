_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K > 1:
            return "".join(sorted(S))
        return min(S[i:] + S[:i] for i in range(len(S)))
