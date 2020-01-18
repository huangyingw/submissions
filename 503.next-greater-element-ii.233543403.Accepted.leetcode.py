class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        next_greater = [-1] * len(nums)
        for i in range(2 * len(nums)):
            num = nums[i % len(nums)]
            while stack and num > nums[stack[-1]]:
                next_greater[stack.pop()] = num
            if i < len(nums):
                stack.append(i)
        return next_greater
