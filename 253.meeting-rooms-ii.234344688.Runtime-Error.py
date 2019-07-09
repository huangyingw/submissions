




import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        heap = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if heap and heap[0] <= interval.start:
                heapq.heapreplace(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
        return len(heap)
