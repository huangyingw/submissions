
class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        num = set(nums)
        for val in num:
            a = nums.count(val)
            if a >= l * 0.5:
                return val
