_author_ = 'jake'
_project_ = 'leetcode'













class Solution:
    def validMountainArray(self, A):

        n = len(A)
        left, right = 0, n - 1
        while left + 1 < n - 1 and A[left + 1] > A[left]:
            left += 1
        while right - 1 > 0 and A[right - 1] > A[right]:
            right -= 1
        return 0 < left == right < n - 1
