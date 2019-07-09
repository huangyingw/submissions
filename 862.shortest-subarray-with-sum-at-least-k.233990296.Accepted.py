_author_ = 'jake'
_project_ = 'leetcode'











from collections import deque


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]
        queue = deque()
        result = n + 1
        for i in range(n + 1):
            while queue and prefix_sums[i] - prefix_sums[queue[0]] >= K:
                result = min(result, i - queue.popleft())
            while queue and prefix_sums[queue[-1]] >= prefix_sums[i]:
                queue.pop()
            queue.append(i)
        return result if result <= n else -1
