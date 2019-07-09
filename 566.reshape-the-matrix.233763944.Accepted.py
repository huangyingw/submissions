_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows, cols = len(nums), len(nums[0])
        if rows * cols != r * c:
            return nums
        reshaped = [[]]
        for i in range(rows):
            for j in range(cols):
                if len(reshaped[-1]) == c:
                    reshaped.append([])
                reshaped[-1].append(nums[i][j])
        return reshaped
