






from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):

        num_count = Counter(nums)
        results = [[]]
        for num in num_count:
            results += [partial + [num] * i for i in range(1, num_count[num] + 1) for partial in results]
        return results
