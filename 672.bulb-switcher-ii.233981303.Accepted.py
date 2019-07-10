













class Solution(object):
    def flipLights(self, n, m):

        if n == 0:
            return 0
        if m == 0:
            return 1
        if m == 1:
            if n == 1:
                return 2
            if n == 2:
                return 3
            return 4
        if m == 2:
            if n == 1:
                return 2
            if n == 2:
                return 4
            if n >= 3:
                return 7
        return 2 ** min(n, 3)
