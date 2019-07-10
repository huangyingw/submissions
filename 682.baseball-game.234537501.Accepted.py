

class Solution:
    def calPoints(self, ops):

        ans = []
        for i in ops:
            if i == 'C':
                ans.pop()
            elif i == '+':
                ans.append(ans[-1] + ans[-2])
            elif i == 'D':
                ans.append(ans[-1] * 2)
            else:
                ans.append(int(i))
        return sum(ans)
