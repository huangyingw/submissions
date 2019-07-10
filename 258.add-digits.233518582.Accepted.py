_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def addDigits(self, num):

        while num > 9:
            num = sum([int(c) for c in str(num)])
        return num
