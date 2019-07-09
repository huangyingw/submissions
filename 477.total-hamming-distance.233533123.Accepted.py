_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hamming = 0
        for bit in range(32):
            set_bits = 0
            for num in nums:
                set_bits += (num >> bit) & 1
            hamming += (n - set_bits) * set_bits
        return hamming
