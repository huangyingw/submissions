class Solution(object):
    def fixedPoint(self, A):
        if not A:
            return -1
        for index, num in enumerate(A):
            if num == index:
                return index
        return -1
