_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findMaximumXOR(self, nums):

        mask = 0
        max_xor = 0
        for bit in range(31, -1, -1):
            mask |= (1 << bit)
            prefixes = {mask & num for num in nums}
            target = max_xor | (1 << bit)
            for prefix in prefixes:
                if prefix ^ target in prefixes:
                    max_xor = target
                    break
        return max_xor
