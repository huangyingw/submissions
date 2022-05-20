class Solution(object):
    def maxProduct(self, nums):
        result = -sys.maxint - 1
        local = 1
        for num in nums:
            local *= num
            result = max(result, local)
        return result
