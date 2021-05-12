class Solution:
    def hIndex(self, citations):
        n = len(citations)
        counts = [0] * (n + 1)
        for i in range(n):
            if citations[i] > n:
                counts[n] += 1
            else:
                counts[citations[i]] += 1
        total = 0
        for i in range(n, -1, -1):
            total += counts[i]
            if total >= i:
                return i
        return 0
