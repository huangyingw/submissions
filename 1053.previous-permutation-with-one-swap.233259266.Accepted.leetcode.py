_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def prevPermOpt1(self, A):

        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                max_seen = -1
                for j in range(len(A) - 1, i, -1):
                    if A[j] >= max_seen and A[j] < A[i]:
                        max_seen = A[j]
                        max_seen_index = j
                A[i], A[max_seen_index] = A[max_seen_index], A[i]
                break
        return A
