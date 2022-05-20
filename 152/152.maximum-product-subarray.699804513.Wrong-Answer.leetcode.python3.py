class Solution(object):
    def maxProduct(self, nums):
        result = float('-inf')
        local = 1
        for num in nums:
            local = max(local * num, num)
            result = max(result, local)
        return result
