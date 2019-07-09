_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, tank, total = 0, 0, 0
        for station in range(len(gas)):
            balance = gas[station] - cost[station]
            tank += balance
            total += balance
            if tank < 0:
                start = station + 1
                tank = 0
        return -1 if total < 0 else start
