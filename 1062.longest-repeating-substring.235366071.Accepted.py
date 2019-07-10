_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def longestRepeatingSubstring(self, S):

        def helper(guess):
            seen = set()
            for i in range(n - guess + 1):
                substring = S[i:i + guess]
                if substring in seen:
                    return True
                seen.add(substring)
            return False
        n = len(S)
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            if helper(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1


class Solution2(object):
    def longestRepeatingSubstring(self, S):
        n = len(S)
        result = 0
        for offset in range(1, n):
            if result >= n - offset:
                break
            sequence = 0
            for i in range(n - offset):
                if S[i] == S[i + offset]:
                    sequence += 1
                    result = max(result, sequence)
                else:
                    sequence = 0
        return result
