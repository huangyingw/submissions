









class Solution(object):
    def minimumDeleteSum(self, s1, s2):

        dp = [0]
        for c in s2:
            dp.append(dp[-1] + ord(c))
        for i in range(len(s1)):
            new_dp = [dp[0] + ord(s1[i])]
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    new_dp.append(dp[j])
                else:
                    new_dp.append(min(ord(s1[i]) + dp[j + 1], ord(s2[j]) + new_dp[-1]))
            dp = new_dp
        return dp[-1]
