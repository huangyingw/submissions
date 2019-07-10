class Solution:
    def findLongestChain(self, pairs):
        current, result = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if current < pair[0]:
                current = pair[1]
                result += 1
        return result
