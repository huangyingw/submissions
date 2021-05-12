class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)
            i += 1
        res.append(newInterval)
        res.extend(intervals[i:])
        return res
