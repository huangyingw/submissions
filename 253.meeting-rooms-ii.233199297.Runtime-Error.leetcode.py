
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        import heapq
        sorted_intervals = sorted(intervals, key=lambda it: (it.start, it.end))
        heap, result = [], 0
        for interval in sorted_intervals:
            start, end = interval.start, interval.end
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            result = max(result, len(heap))
        return result
