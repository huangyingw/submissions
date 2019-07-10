













class Solution:
    def maxTurbulenceSize(self, A):

        if len(A) == 1:
            return 1
        result = 0
        down, up = 0, 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                up += 1
                down = 0
            elif A[i] < A[i - 1]:
                down += 1
                up = 0
            else:
                down = 0
                up = 0
            result = max(result, up, down)
            up, down = down, up
        return result + 1 if result != 0 else 0
