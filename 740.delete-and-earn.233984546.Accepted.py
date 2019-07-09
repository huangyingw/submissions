_author_ = 'jake'
_project_ = 'leetcode'












from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        pairs = [(num, count) for num, count in freq.items()]
        pairs.sort()
        used, not_used = 0, 0
        for i, (num, count) in enumerate(pairs):
            if i == 0 or pairs[i - 1][0] != num - 1:
                not_used = max(used, not_used)
                used = num * count + not_used
            else:
                used, not_used = num * count + not_used, max(used, not_used)
        return max(used, not_used)
