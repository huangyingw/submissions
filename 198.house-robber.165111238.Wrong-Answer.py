class Solution(object):
    def rob(self, nums):
        last = now = 0
        for num in nums:
            now = max(last + num, now)
            last = now
        return now
