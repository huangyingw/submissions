from collections import Counter


class Solution(object):
    def largestUniqueNumber(self, A):
        freq = Counter(A)
        unique = [key for key, val in freq.items() if val == 1]
        if not unique:
            return -1
        return max(unique)
