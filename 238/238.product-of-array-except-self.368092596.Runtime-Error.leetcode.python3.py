from functools import reduce


class Solution:
    def productExceptSelf(self, nums):
        def mutifly(a, b):
            return a * b
        if all(nums):
            product = reduce(mutifly, nums)
            return [product // n for n in nums]
        else:
            ret = [0] * len(nums)
            if nums.count(0) == 1:
                i = nums.index(0)
                nums[i] = 1
                ret[i] = reduce(mutifly, nums)
            return ret

    def productExceptSelf2(self, nums):
        p = 1
        n = len(nums)
        ret = []
        for i in range(0, n):
            ret.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            ret[i] = ret * p
            p = p * nums[i]
        return ret
    input_array = [1, 2, 3, 4]
    output_array = [24, 12, 8, 6]
    assert t.productExceptSelf(input_array) == output_array
    input_array = [1, 2, 3, 0]
    output_array = [0, 0, 0, 6]
    assert t.productExceptSelf(input_array) == output_array
