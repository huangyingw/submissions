_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        operations = 0
        while Y > X:
            operations += 1
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
        return X - Y + operations
