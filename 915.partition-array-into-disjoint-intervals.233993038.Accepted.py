class Solution:
    def partitionDisjoint(self, A):
        last_left = 0
        max_left = max_overall = A[0]
        for i, num in enumerate(A[1:], 1):
            max_overall = max(max_overall, num)
            if num < max_left:
                last_left = i
                max_left = max_overall
        return last_left + 1
