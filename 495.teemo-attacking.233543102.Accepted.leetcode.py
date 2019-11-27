class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        poisoned = 0
        timeSeries.append(float("inf"))
        for i in range(1, len(timeSeries)):
            poisoned += min(duration, timeSeries[i] - timeSeries[i - 1])
        return poisoned
