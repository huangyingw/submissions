






class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        overlap = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if overlap and overlap[-1].end > interval.start:
                return False
            else:
                overlap.append(interval)
        return True
