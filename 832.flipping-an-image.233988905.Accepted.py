_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            result.append([1 - val for val in reversed(row)])
        return result
