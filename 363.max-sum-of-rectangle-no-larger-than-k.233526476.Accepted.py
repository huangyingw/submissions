









import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):

        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float("-inf")
        for i in range(cols):
            row_sums = [0 for _ in range(rows)]
            for j in range(i, cols):
                sorted_sums = [0]
                all_row_sum = 0
                for r in range(rows):
                    row_sums[r] += matrix[r][j]
                    all_row_sum += row_sums[r]
                    larger = bisect.bisect_left(sorted_sums, all_row_sum - k)
                    if larger != len(sorted_sums):
                        if all_row_sum - sorted_sums[larger] == k:
                            return k
                        max_sum = max(max_sum, all_row_sum - sorted_sums[larger])
                    bisect.insort_left(sorted_sums, all_row_sum)
        return max_sum
