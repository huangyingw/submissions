_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1]
        for i in range(1, len(nums)):
            products.append(nums[i - 1] * products[-1])
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]
        return products
