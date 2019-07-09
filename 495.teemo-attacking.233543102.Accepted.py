_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poisoned = 0
        timeSeries.append(float("inf"))
        for i in range(1, len(timeSeries)):
            poisoned += min(duration, timeSeries[i] - timeSeries[i - 1])
        return poisoned
