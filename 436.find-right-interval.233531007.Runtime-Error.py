












class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):

        intervals = [[intervals[i], i] for i in range(len(intervals))]
        intervals.sort(key=lambda x: x[0].start)
        result = [-1] * len(intervals)
        for interval, i in intervals:
            left, right = 0, len(intervals)
            while left < right:
                mid = (left + right) // 2
                if intervals[mid][0].start < interval.end:
                    left = mid + 1
                else:
                    right = mid
            if left == len(intervals):
                continue
            result[i] = intervals[left][1]
        return result
