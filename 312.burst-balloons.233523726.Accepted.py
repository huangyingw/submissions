












class Solution(object):
    def maxCoins(self, nums):

        n = len(nums)
        nums = [1] + nums + [1]
        max_coins = [[0 for _ in range(n + 2)] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for left in range(1, n + 2 - length):
                right = left + length - 1
                for last in range(left, right + 1):
                    this_coins = nums[left - 1] * nums[last] * nums[right + 1]
                    max_coins[length][left] = max(max_coins[length][left],
                                                  this_coins + max_coins[last - left][left] + max_coins[right - last][last + 1])
        return max_coins[-1][1]
