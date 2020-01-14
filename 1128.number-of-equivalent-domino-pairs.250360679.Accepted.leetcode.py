from collections import defaultdict
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        seen = defaultdict(int)
        result = 0
        for domino in dominoes:
            if domino[0] > domino[1]:
                domino = domino[::-1]
            domino_tuple = tuple(domino)
            result += seen[domino_tuple]
            seen[domino_tuple] += 1
        return result
