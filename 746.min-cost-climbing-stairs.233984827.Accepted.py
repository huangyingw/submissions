









class Solution(object):
    def minCostClimbingStairs(self, cost):

        prev, step = cost[:2]
        for c in cost[2:]:
            prev, step = step, c + min(prev, step)
        return min(prev, step)
