class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def insert(self, intervals, newInterval):
        left, right = 0, len(intervals) - 1
        while left < len(intervals) and intervals[left].end < newInterval.start:
            left += 1
        while right >= 0 and intervals[right].start > newInterval.end:
            right -= 1
        if left <= right:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)
        return intervals[:left] + [newInterval] + intervals[right + 1:]
