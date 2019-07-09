_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(s) for s in nums]
        result = nums[0]
        if len(nums) == 1:
            return result
        if len(nums) == 2:
            return result + "/" + nums[1]
        return result + "/(" + "/".join(nums[1:]) + ")"
