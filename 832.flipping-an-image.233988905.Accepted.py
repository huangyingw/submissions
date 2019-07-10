










class Solution(object):
    def flipAndInvertImage(self, A):

        result = []
        for row in A:
            result.append([1 - val for val in reversed(row)])
        return result
