class Solution(object):
    def maxRotateFunction(self, A):
        rotate_val, sum_A = 0, 0
        for i, num in enumerate(A):
            sum_A += num
            rotate_val += i * num
        max_rotate = rotate_val
        for i in range(len(A) - 1, -1, -1):
            rotate_val += sum_A - (len(A) * A[i])
            max_rotate = max(max_rotate, rotate_val)
        return max_rotate
