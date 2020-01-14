class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = []
        left2right = []
        right2left = []
        tmpnumL = 1
        tmpnumR = 1
        for i in range(0, n):
            left2right.append(tmpnumL)
            tmpnumL = tmpnumL * nums[i]
            right2left.append(tmpnumR)
            tmpnumR = tmpnumR * nums[(n - 1) - i]
        for i in range(0, n):
            output.append(right2left[(n - 1) - i] * left2right[i])
        return output
class Solution2:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n
        tmpnumL = 1
        tmpnumR = 1
        for i in range(0, n - 1):
            tmpnumL = tmpnumL * nums[i]
            output[i + 1] = tmpnumL
        for i in range((n - 1), 0, -1):
            tmpnumR = tmpnumR * nums[i]
            output[i - 1] *= tmpnumR
        return output
