from collections import defaultdict
class Solution(object):
    def longestSubsequence(self, arr, difference):
        num_to_length = defaultdict(int)
        for num in arr:
            num_to_length[num] = num_to_length[num - difference] + 1
        return max(num_to_length.values())
