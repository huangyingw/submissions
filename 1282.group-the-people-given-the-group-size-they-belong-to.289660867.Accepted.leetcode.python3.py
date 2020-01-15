from collections import defaultdict


class Solution(object):
    def groupThePeople(self, groupSizes):
        size_to_group = defaultdict(list)
        result = []
        for i, size in enumerate(groupSizes):
            size_to_group[size].append(i)
            if len(size_to_group[size]) == size:
                result.append(size_to_group[size])
                size_to_group[size] = []
        return result
