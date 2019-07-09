_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        cheapest = [[float("inf"), []] for _ in range(len(A))]
        cheapest[0] = [A[0], [1]]
        for i, cost in enumerate(A[:-1]):
            if cost == -1:
                continue
            for j in range(i + 1, min(i + B + 1, len(A))):
                if A[j] == -1:
                    continue
                new_cost = cheapest[i][0] + A[j]
                new_path = cheapest[i][1] + [j + 1]
                cheapest[j] = min(cheapest[j], [new_cost, new_path])
        return cheapest[-1][1]
