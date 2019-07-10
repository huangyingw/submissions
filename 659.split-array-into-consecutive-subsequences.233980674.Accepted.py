_author_ = 'jake'
_project_ = 'leetcode'








from collections import Counter, defaultdict


class Solution(object):
    def isPossible(self, nums):

        freq = Counter(nums)
        sequences = defaultdict(int)
        for num in nums:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            if sequences[num - 1] != 0:
                sequences[num - 1] -= 1
                sequences[num] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                sequences[num + 2] += 1
            else:
                return False
        return True
