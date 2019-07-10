'''
	Given a collection of intervals, merge all overlapping intervals.
	Example 1:
	Input: [[1,3],[2,6],[8,10],[15,18]]
	Output: [[1,6],[8,10],[15,18]]
	Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
	Example 2:
	Input: [[1,4],[4,5]]
	Output: [[1,5]]
	Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''







class compare(object):
    def __init__(self, interval):
        self.interval = interval

    def __lt__(self, other):
        if self.interval.start == other.interval.start:
            return self.interval.end < other.interval.end
        return self.interval.start < other.interval.end


class Solution(object):
    def merge(self, intervals):

        intervals = sorted(intervals, key=compare)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged
