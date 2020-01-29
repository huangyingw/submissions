class Solution(object):
    def numberOfWays(self, num_people):
        dp = [1]
        for people in range(2, num_people + 1, 2):
            result = 0
            for left in range(0, people - 1, 2):
                result += dp[left / 2] * dp[(people - left - 2) / 2]
            dp.append(result)
        return dp[-1] % (10 ** 9 + 7)
