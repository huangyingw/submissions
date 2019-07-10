



class Solution:
    def minFlipsMonoIncr(self, S):

        n = len(S)
        cnt0 = S.count('0')
        cnt1 = 0
        res = n - cnt0
        for i in range(n):
            if S[i] == '0':
                cnt0 -= 1
            elif S[i] == '1':
                res = min(res, cnt1 + cnt0)
                cnt1 += 1
        return res
