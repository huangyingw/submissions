from collections import defaultdict


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        count = 0
        subsequences = []
        for i in range(len(A)):
            subsequences.append(defaultdict(int))
            for j in range(i):
                diff = A[i] - A[j]
                diff_count = subsequences[j].get(diff, 0)
                count += diff_count
                subsequences[-1][diff] += diff_count + 1
        return count
