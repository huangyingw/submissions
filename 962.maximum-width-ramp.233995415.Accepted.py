












class Solution(object):
    def maxWidthRamp(self, A):

        max_ramp = 0
        stack = []
        for i, num in enumerate(A):
            if not stack or num < A[stack[-1]]:
                stack.append(i)
        for i in range(len(A) - 1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                max_ramp = max(max_ramp, i - stack.pop())
        return max_ramp
