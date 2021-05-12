from collections import Counter


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1_counts = Counter(arr1)
        result = []
        for val in arr2:
            if val in arr1_counts:
                result += [val] * arr1_counts[val]
                del arr1_counts[val]
        for val in sorted(arr1_counts.keys()):
            result += [val] * arr1_counts[val]
        return result
