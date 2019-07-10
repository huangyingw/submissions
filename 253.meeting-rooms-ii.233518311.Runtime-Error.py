_author_ = 'jake'
_project_ = 'leetcode'













class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):

        max_rooms = 0
        rooms = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            heapq.heappush(rooms, interval.end)
            while rooms[0] <= interval.start:
                heapq.heappop(rooms)
            max_rooms = max(max_rooms, len(rooms))
        return max_rooms


class Solution2(object):
    def minMeetingRooms(self, intervals):
        overlaps = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if overlaps and interval.start >= overlaps[0]:
                heapq.heapreplace(overlaps, interval.end)
            else:
                heapq.heappush(overlaps, interval.end)
        return len(overlaps)
