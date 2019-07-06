class Solution(object):
    def rob(self, nums):
        now = last = 0
        for i in nums:
            last, now = now, max(i + last, now)
        return now
