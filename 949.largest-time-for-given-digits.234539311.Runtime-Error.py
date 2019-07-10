import itertools


class Solution2:
    def largestTimeFromDigits(self, A):
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time
        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""


class Solution3:
    def largestTimeFromDigits(self, A):
        return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
