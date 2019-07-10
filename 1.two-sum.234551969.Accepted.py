


class Solution:
    def twoSum(self, nums, target):
        n = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in n:
                return [n[temp], index]
            n[num] = index
