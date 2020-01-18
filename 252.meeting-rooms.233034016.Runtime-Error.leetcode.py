class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x.start)
        ls = len(intervals)
        for i in range(ls - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
