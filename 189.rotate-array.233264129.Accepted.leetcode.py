class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
class Solution2(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
