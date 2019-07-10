_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def numsSameConsecDiff(self, N, K):

        partials = [i for i in range(1, 10)]
        for _ in range(N - 1):
            new_partials = []
            for p in partials:
                last_digit = p % 10
                if last_digit - K >= 0:
                    new_partials.append(p * 10 + last_digit - K)
                if K != 0 and last_digit + K < 10:
                    new_partials.append(p * 10 + last_digit + K)
            partials = new_partials
        if N == 1:
            partials.append(0)
        return partials
