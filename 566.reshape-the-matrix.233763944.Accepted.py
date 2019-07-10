class Solution(object):
    def matrixReshape(self, nums, r, c):
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
