






















class Solution(object):
    def soupServings(self, N):

        memo = {}

        def helper(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1
            if B <= 0:
                return 0
            if (A, B) in memo:
                return memo[(A, B)]
            result = 0.25 * (helper(A - 4, B) + helper(A - 3, B - 1) + helper(A - 2, B - 2) + helper(A - 1, B - 3))
            memo[(A, B)] = result
            return result
        portions = math.ceil(N / float(25))
        if N > 4800:
            return 1
        return helper(portions, portions)
