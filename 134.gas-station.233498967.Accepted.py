class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start, tank, total = 0, 0, 0
        for station in range(len(gas)):
            balance = gas[station] - cost[station]
            tank += balance
            total += balance
            if tank < 0:
                start = station + 1
                tank = 0
        return -1 if total < 0 else start
