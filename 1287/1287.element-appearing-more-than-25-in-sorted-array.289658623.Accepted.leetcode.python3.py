from collections import defaultdict


class Solution(object):
    def findSpecialInteger(self, arr):
        target = len(arr) // 4 + 1
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
            if counts[num] == target:
                return num
