class Solution(object):
    def rotate(self, nums, k):
        def reverse(nums, left, right):
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
