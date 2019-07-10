_author_ = 'jake'
_project_ = 'leetcode'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [i, num_to_index[target - num]]
            num_to_index[num] = i
        return []
