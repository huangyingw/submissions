import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        dp = [[0, 0]]
        jobs = sorted(zip(endTime, startTime, profit))
        for end, start, gain in jobs:
            i = bisect.bisect_right(dp, [start, float("inf")])
            if gain + dp[i - 1][1] > dp[-1][1]:
                dp.append([end, gain + dp[i - 1][1]])
        return dp[-1][1]
