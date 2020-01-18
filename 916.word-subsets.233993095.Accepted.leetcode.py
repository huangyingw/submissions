from collections import Counter, defaultdict


class Solution:
    def wordSubsets(self, A, B):
        required = defaultdict(int)
        for b in B:
            freq = Counter(b)
            for letter, count in freq.items():
                required[letter] = max(required[letter], count)
        results = []
        for a in A:
            freq = Counter(a)
            if all(freq[letter] >= count for letter, count in required.items()):
                results.append(a)
        return results
