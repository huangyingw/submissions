_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(a for a, _ in costs[:n]) + sum(b for _, b in costs[n:])
