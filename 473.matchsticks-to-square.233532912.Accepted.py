_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(index):
            if index == len(nums):
                return True
            for side in range(4):
                if sides[side] + nums[index] > target or sides[side] in sides[side + 1:]:
                    continue
                sides[side] += nums[index]
                if dfs(index + 1):
                    return True
                sides[side] -= nums[index]
            return False
        perimeter = sum(nums)
        target, remainder = divmod(perimeter, 4)
        if not perimeter or remainder:
            return False
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        sides = [0] * 4
        i = 0
        while i < 4 and nums[i] == target:
            sides[i] = target
            i += 1
        return dfs(i)
