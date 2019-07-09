_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        ones = 0
        block_size = 10
        for _ in range(len(str(n))):
            blocks, rem = divmod(n + 1, block_size)
            ones += blocks * block_size // 10
            ones += min(block_size // 10, max(0, rem - block_size // 10))
            block_size *= 10
        return ones
