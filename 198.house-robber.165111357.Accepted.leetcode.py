class Solution(object):
    def rob(self, nums):
        last = now = 0
        for num in nums:
            temp = now
            now = max(last + num, now)
            last = temp
        return now
