_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def countBits(self, num):

        ones = [0]
        for i in range(1, num + 1):
            ones.append(1 + ones[i & (i - 1)])
        return ones
