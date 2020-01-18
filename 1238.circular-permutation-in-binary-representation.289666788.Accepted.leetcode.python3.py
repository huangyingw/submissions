class Solution(object):
    def circularPermutation(self, n, start):
        def helper(i):
            if i == 1:
                return [0, 1]
            temp = helper(i - 1)
            power = 2 ** (i - 1)
            return temp + [power + t for t in temp[::-1]]
        perms = helper(n)
        i = perms.index(start)
        return perms[i:] + perms[:i]
