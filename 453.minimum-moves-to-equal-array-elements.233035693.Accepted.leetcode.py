class Solution(object):
    def minMoves(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        min_num = min(nums)
        return sum([i - min_num for i in nums])
