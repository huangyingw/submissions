from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        counts = Counter(text)
        result = float("inf")
        for c, count in Counter("balloon").items():
            result = min(result, counts[c] // count)
        return result
