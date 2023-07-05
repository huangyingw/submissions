class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        stack = []
        left = [0] * n
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1] + 1
            else:
                left[i] = 0
            stack.append(i)
        stack = []
        right = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - 1
            else:
                right[i] = n - 1
            stack.append(i)
        res = 0
        for i in range(n):
            res = max(res, nums[i] * (presum[right[i] + 1] - presum[left[i]]))
        return res % (10**9 + 7)
