class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) // 2]
    def majorityElement(self, nums):
        l = len(nums)
        num = set(nums)
        for val in num:
            a = nums.count(val)
            if a >= l * 0.5:
                return val
