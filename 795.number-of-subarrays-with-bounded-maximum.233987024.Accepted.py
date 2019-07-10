











class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):

        subarrays, total = 0, 0
        last_above_max = -1
        for i, num in enumerate(A):
            if num > R:
                subarrays = 0
                last_above_max = i
            elif num < L:
                total += subarrays
            else:
                subarrays = i - last_above_max
                total += subarrays
        return total
