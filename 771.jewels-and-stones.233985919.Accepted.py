_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(1 for s in S if s in set(J))
