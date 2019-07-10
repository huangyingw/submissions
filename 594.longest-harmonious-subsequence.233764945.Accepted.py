







from collections import Counter


class Solution(object):
    def findLHS(self, nums):

        freq = Counter(nums)
        max_harmonious = 0
        for num, count in freq.items():
            if num + 1 in freq:
                max_harmonious = max(max_harmonious, count + freq[num + 1])
        return max_harmonious
