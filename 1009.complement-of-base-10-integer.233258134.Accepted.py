_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def bitwiseComplement(self, N):

        if N == 0:
            return 1
        return (2**N.bit_length() - 1) - N
