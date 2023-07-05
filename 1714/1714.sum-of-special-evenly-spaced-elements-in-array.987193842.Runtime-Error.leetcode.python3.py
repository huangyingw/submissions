class Solution:
    def maxSumEvenlySpaced(self, nums, k):

        n = len(nums)
        max_sum = 0
        result = []
        for i in range(0, n - k + 1, k):
            current_sum = 0
            for j in range(i, i + k):
                current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
            result.append(max_sum)
        return result

    def solve(self, nums, queries):

        result = []
        for query in queries:
            start = query[0]
            end = query[1]
            result.append(
                self.maxSumEvenlySpaced(nums[start: end + 1], end - start + 1)
            )
        return list(map(int, result))
