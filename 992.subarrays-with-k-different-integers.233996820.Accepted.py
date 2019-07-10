_author_ = 'jake'
_project_ = 'leetcode'












from collections import Counter


class Solution(object):
    def subarraysWithKDistinct(self, A, K):

        def at_most_k(distinct):
            count = Counter()
            subarrays = 0
            start = 0
            for end, num in enumerate(A):
                if count[num] == 0:
                    distinct -= 1
                count[num] += 1
                while distinct < 0:
                    count[A[start]] -= 1
                    if count[A[start]] == 0:
                        distinct += 1
                    start += 1
                subarrays += end - start + 1
            return subarrays
        return at_most_k(K) - at_most_k(K - 1)
