from collections import defaultdict


class Solution(object):
    def canConvert(self, str1, str2):
        if len(set(str2)) == 26 and str1 != str2:
            return False
        char1_indices = defaultdict(list)
        for i, c in enumerate(str1):
            char1_indices[c].append(i)
        for c, indices in char1_indices.items():
            if len({str2[i] for i in indices}) != 1:
                return False
        return True
