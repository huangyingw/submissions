class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        next_greater = [-1] * n
        for i in range(2 * n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                next_greater[stack.pop()] = num
            if i < n:
                stack.append(i)
        return next_greater
