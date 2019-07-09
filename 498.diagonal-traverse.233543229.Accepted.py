_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        diagonal = []
        if not matrix or not matrix[0]:
            return diagonal
        rows, cols = len(matrix), len(matrix[0])
        up_right = True
        r, c = 0, 0
        while len(diagonal) < rows * cols:
            diagonal.append(matrix[r][c])
            if up_right:
                if c == cols - 1:
                    r += 1
                    up_right = False
                elif r == 0:
                    c += 1
                    up_right = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1:
                    c += 1
                    up_right = True
                elif c == 0:
                    r += 1
                    up_right = True
                else:
                    r += 1
                    c -= 1
        return diagonal
