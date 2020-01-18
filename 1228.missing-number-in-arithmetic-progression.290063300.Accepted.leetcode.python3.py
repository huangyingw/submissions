class Solution(object):
    def missingNumber(self, arr):
        first_diff = arr[1] - arr[0]
        if first_diff == 2 * (arr[2] - arr[1]):
            return arr[0] + first_diff // 2
        for i in range(1, len(arr) - 1):
            if (arr[i + 1] - arr[i]) == first_diff * 2:
                return arr[i] + first_diff
