class Solution(object):
    def maxProduct(self, nums):
        result = 0
        local = 1
        for num in nums:
            local *= num
            result = max(result, local)
        return result
