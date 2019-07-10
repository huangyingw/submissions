_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def splitArraySameAverage(self, A):

        def n_sum_target(n, tgt, j):
            if (n, tgt, j) in invalid:
                return False
            if n == 0:
                return tgt == 0
            for i in range(j, len(C)):
                if C[i] > tgt:
                    break
                if n_sum_target(n - 1, tgt - C[i], i + 1):
                    return True
            invalid.add((n, tgt, j))
            return False
        n, sum_A = len(A), sum(A)
        invalid = set()
        C = sorted(A)
        for len_B in range(1, (n // 2) + 1):
            target = sum_A * len_B / float(n)
            if target != int(target):
                continue
            if n_sum_target(len_B, target, 0):
                return True
        return False
