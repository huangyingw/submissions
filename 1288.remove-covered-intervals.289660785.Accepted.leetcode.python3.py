class Solution(object):
    def removeCoveredIntervals(self, intervals):
        stack = []
        intervals.sort()
        for interval in intervals:
            if not stack or stack[-1][1] < interval[1]:
                stack.append(interval)
        return len(stack)
