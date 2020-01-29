import time


class Solution(object):
    def getFactors(self, n):
        return self.factorise(n, 2, [], [])

    def factorise(self, n, trial, partial, factors):
        while trial * trial <= n:
            if n % trial == 0:
                factors.append(partial + [n // trial, trial])
                self.factorise(n // trial, trial, partial + [trial], factors)
            trial += 1
        return factors


class Solution2(object):
    def getFactors(self, n):
        stack = [(n, 2, [])]
        factors = []
        while stack:
            num, trial, partial = stack.pop()
            while trial * trial <= num:
                if num % trial == 0:
                    factors.append(partial + [num // trial, trial])
                    stack.append((num // trial, trial, partial + [trial]))
                trial += 1
        return factors
