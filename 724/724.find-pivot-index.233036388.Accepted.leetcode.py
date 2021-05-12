class Solution(object):
    def pivotIndex(self, nums):
        totalsum = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            if leftsum == totalsum - leftsum - v:
                return i
            leftsum += v
        return -1
