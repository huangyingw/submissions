



class Solution:
    def powerfulIntegers(self, x, y, bound):

        ans = set()

        for i in range(20):
            for j in range(20):
                v = x ** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)
