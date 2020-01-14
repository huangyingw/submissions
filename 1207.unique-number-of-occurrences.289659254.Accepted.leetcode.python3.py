from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        counts = Counter(arr)
        return len(set(counts.values())) == len(counts.values())
