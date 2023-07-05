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


def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    k = 3
    main()
