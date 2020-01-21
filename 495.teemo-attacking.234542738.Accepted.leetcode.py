class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0:
            return 0
        return sum(min(duration, i - j) for i, j in zip(timeSeries[1:], timeSeries[:-1])) + duration

    def findPoisonedDuration(self, timeSeries, duration):
        return sum(min(duration, b - a) for a, b in zip(timeSeries, timeSeries[1:] + [10e7]))
    assert t.findPoisonedDuration([1, 4], 2) == 4
    assert t.findPoisonedDuration([], 1000) == 0
