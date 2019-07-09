_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or N >= K + W:
            return 1
        probability = [0] * (N + 1)
        probability[0] = 1.0
        window = 1.0
        for i in range(1, N + 1):
            probability[i] = window / W
            if i < K:
                window += probability[i]
            if i - W >= 0:
                window -= probability[i - W]
        return sum(probability[K:])
