_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev, step = cost[:2]
        for c in cost[2:]:
            prev, step = step, c + min(prev, step)
        return min(prev, step)
