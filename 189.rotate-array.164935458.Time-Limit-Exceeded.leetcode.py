class Solution(object):
    def rotate(self, nums, k):
        def reverse(left, right):
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
