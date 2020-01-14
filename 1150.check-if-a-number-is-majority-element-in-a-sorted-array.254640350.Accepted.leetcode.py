import bisect
class Solution(object):
    def isMajorityElement(self, nums, target):
        n = len(nums)
        i = bisect.bisect_left(nums, target)
        if i == n or nums[i] != target:
            return False
        return nums[(i + n // 2) % n] == target
