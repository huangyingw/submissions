class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        start_index = 0
        for end_index in range(0, len(A)):
            K -= 1 - A[end_index]
            if K < 0:
                K += 1 - A[start_index]
                start_index += 1
        return end_index - start_index + 1
