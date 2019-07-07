class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            num = abs(num)                          # may be negative so take absolute value
            nums[num - 1] = -abs(nums[num - 1])     # set nums[num - 1] to indicate num - 1 seen
        return [i + 1 for i, num in enumerate(nums) if num > 0]
