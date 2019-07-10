_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def canAttendMeetings(self, intervals):

        intervals.sort(key=lambda x: x.start)
        for i, interval in enumerate(intervals[1:], 1):
            if interval.start < intervals[i - 1].end:
                return False
        return True
