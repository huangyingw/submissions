_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


class Solution2(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
