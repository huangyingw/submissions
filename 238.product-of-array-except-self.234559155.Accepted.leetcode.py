class Solution(object):
    def productExceptSelf(self, nums):
        totalProduct = reduce((lambda total, num: total * num), nums)
        if totalProduct:
            return map((lambda num: totalProduct / num), nums)
        else:
            totalProduct = []
            for i in range(len(nums)):
                totalProduct.append(reduce((lambda total, num: total * num), \
                                           [num for index, num in enumerate(nums) if index != i]))
            return totalProduct
