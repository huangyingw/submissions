











class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        erase = 0
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        current_end = intervals[0].start
        for interval in intervals:
            if current_end > interval.start:
                erase += 1
                if interval.end > current_end:
                    continue
            current_end = interval.end
        return erase
