class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        results = []
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                results = []
            if diff == min_diff:
                results.append([arr[i - 1], arr[i]])
        return results
