_author_ = 'jake'
_project_ = 'leetcode'








from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):

        if k < 0:
            return 0
        freq = Counter(nums)
        pairs = 0
        for num in freq:
            if k == 0:
                if freq[num] > 1:
                    pairs += 1
            else:
                if num + k in freq:
                    pairs += 1
        return pairs
