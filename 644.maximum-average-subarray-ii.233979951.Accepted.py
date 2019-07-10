












class Solution(object):
    def findMaxAverage(self, nums, k):

        n = len(nums)
        if k < 80:
            cumulative = [0]
            for num in nums:
                cumulative.append(cumulative[-1] + num)
            result = float('-inf')
            for length in range(k, min(n + 1, 2 * k)):
                max_sum = max([cumulative[length + i] - cumulative[i] for i in range(n - length + 1)])
                result = max(result, max_sum / float(length))
            return result

        def has_average(x):
            subarray_sum = 0
            for i in range(k):
                subarray_sum += nums[i] - x
            if subarray_sum >= 0:
                return True
            prefix_sum, min_prefix = 0, 0
            for i in range(k, n):
                subarray_sum += nums[i] - x
                prefix_sum += nums[i - k] - x
                min_prefix = min(min_prefix, prefix_sum)
                if subarray_sum - min_prefix >= 0:
                    return True
            return False
        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right) / 2.0
            if has_average(mid):
                left = mid
            else:
                right = mid
        return left
