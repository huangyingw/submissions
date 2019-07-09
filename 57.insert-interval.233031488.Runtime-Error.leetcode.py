
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
            if newInterval.start > interval.end:
                result.append(interval)
            elif newInterval.end < interval.start:
                result.append(newInterval)
                newInterval = interval
            elif newInterval.start <= interval.end or newInterval.end >= interval.start:
                newInterval = Interval(min(newInterval.start, interval.start), max(interval.end, newInterval.end))
        result.append(newInterval)
        return result
