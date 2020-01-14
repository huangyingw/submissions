class Solution(object):
    def numDupDigitsAtMostN(self, N):
        digits = [int(c) for c in str(N + 1)]
        n = len(digits)
        not_dup = 0
        def permutations(num_digits, length):
            if length == 0:
                return 1
            return permutations(num_digits, length - 1) * (num_digits - length + 1)
        for i in range(1, n):
            not_dup += 9 * permutations(9, i - 1)
        seen = set()
        for i, max_digit in enumerate(digits):
            for digit in range(0 if i else 1, max_digit):
                if digit not in seen:
                    not_dup += permutations(9 - i, n - i - 1)
            if max_digit in seen:
                break
            seen.add(max_digit)
        return N - not_dup
