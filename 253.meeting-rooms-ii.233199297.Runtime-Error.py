'''
	Given an array of meeting time intervals consisting of start and end times [[s1,e1], [s2,e2],…] (si < ei), find the minimum number of conference rooms required.
	For example,
	Given [[0, 30],[5, 10],[15, 20]],
	return 2.
'''


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
