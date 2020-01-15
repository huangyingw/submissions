class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        def kadane(arr):
            curr_sum, max_sum = arr[0], arr[0]
            for index in range(1, len(arr)):
                curr_sum = max(arr[index], curr_sum + arr[index])
                max_sum = max(max_sum, curr_sum)
            return max_sum

        def prefix(arr):
            curr_sum, max_val = 0, float('-inf')
            for index, val in enumerate(arr):
                curr_sum += val
                max_val = max(max_val, curr_sum)
            return max_val

        def suffix(arr):
            curr_sum, max_val = 0, float('-inf')
            for index in range(len(arr) - 1, -1, -1):
                curr_sum += arr[index]
                max_val = max(max_val, curr_sum)
            return max_val
        if not arr:
            return 0
        if k == 1:
            return max(0, kadane(arr)) % (10 ** 9 + 7)
        else:
            return max(0, max((prefix(arr) + suffix(arr) + (k - 2) * max(sum(arr), 0), kadane(arr)))) % (10 ** 9 + 7)
