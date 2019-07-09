_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [0]
        max_reach = -1
        while stack:
            index = stack.pop()
            if index + nums[index] > max_reach:
                if index + nums[index] >= len(nums) - 1:
                    return True
                for i in range(index + nums[index], max_reach, -1):
                    stack.append(i)
                max_reach = index + nums[index]
        return False
