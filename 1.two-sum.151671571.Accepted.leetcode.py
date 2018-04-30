class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx, val in enumerate(nums):
            if target - val in dict:
                return (dict[target - val], idx)
            dict[val] = idx

