class Solution(object):
    def minSwap(self, A, B):
        prev_no_swap, prev_swap = 0, 1
        for i in range(1, len(A)):
            no_swap, swap = float("inf"), float("inf")
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                no_swap = prev_no_swap
                swap = 1 + prev_swap
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                no_swap = min(no_swap, prev_swap)
                swap = min(swap, 1 + prev_no_swap)
            prev_no_swap, prev_swap = no_swap, swap
        return min(prev_no_swap, prev_swap)
