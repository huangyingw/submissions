class Solution(object):
    def findLength(self, A, B):
        def mutual_subarray(length):
            subarrays = set(tuple(A[i:i + length])
                            for i in range(len(A) - length + 1))
            return any(tuple(B[j:j + length]) in subarrays
                       for j in range(len(B) - length + 1))
        low, high = 0, min(len(A), len(B)) + 1
        while low < high:
            mid = (low + high) // 2
            if mutual_subarray(mid):
                low = mid + 1
            else:
                high = mid
        return low - 1
