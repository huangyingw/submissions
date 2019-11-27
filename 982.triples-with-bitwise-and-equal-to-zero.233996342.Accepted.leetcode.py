from collections import defaultdict


class Solution:
    def countTriplets(self, A):
        pairs = defaultdict(int)
        for num1 in A:
            for num2 in A:
                pairs[num1 & num2] += 1
        result = 0
        for pair, count in pairs.items():
            for num3 in A:
                if pair & num3 == 0:
                    result += count
        return result
