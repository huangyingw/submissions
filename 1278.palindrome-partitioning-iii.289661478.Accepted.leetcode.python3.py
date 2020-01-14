class Solution(object):
    def palindromePartition(self, s, k):
        n = len(s)
        def cost(left, right):
            result = 0
            while left < right:
                if s[left] != s[right]:
                    result += 1
                left += 1
                right -= 1
            return result
        memo = {}
        def helper(i, k):
            if k >= n - i:
                return 0
            if k == 1:
                return cost(i, n - 1)
            if (i, k) in memo:
                return memo[(i, k)]
            chars_changed = float("inf")
            for j in range(i, n - k + 1):
                chars_changed = min(chars_changed, cost(i, j) + helper(j + 1, k - 1))
            memo[(i, k)] = chars_changed
            return chars_changed
        return helper(0, k)
