































class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        timeline = []
        for interval in intervals:

            timeline.append((interval.start, 1))

            timeline.append((interval.end, -1))

        timeline.sort()
        ans = curr = 0

        for _, v in timeline:
            curr += v

            ans = max(ans, curr)
        return ans
