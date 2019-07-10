











from collections import defaultdict
import bisect


class Solution(object):
    def shortestWay(self, source, target):

        char_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)
        result = 0
        i = 0
        for c in target:
            if c not in char_indices:
                return -1
            j = bisect.bisect_left(char_indices[c], i)
            if j == len(char_indices[c]):
                result += 1
                j = 0
            i = char_indices[c][j] + 1
        return result if i == 0 else result + 1
