_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lengths, counts = [], []
        for i, num in enumerate(nums):
            length, count = 1, 1
            for j in range(i):
                if num > nums[j]:
                    if lengths[j] + 1 > length:
                        length = lengths[j] + 1
                        count = counts[j]
                    elif lengths[j] + 1 == length:
                        count += counts[j]
            lengths.append(length)
            counts.append(count)
        longest = max(lengths)
        return sum([count for length, count in zip(lengths, counts) if length == longest])
