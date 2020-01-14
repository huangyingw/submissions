class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)
        column = len(matrix[0])
        i, j = 0, column - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
    def searchMatrix2(self, matrix, target):
        if not matrix:
            return False
        if not matrix[0]:
            return False
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if matrix[mid][0] < target:
                left = mid
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return True
        index = left
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[index][mid] < target:
                left = mid + 1
            elif matrix[index][mid] > target:
                right = mid - 1
            else:
                return True
        return False
