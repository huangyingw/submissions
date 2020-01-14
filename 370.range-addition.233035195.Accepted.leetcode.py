class Solution(object):
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for t in updates:
            start, end, val = t
            res[start] += val
            if end < length - 1:
                res[end + 1] -= val
        for i in range(1, length):
            res[i] = res[i] + res[i - 1]
        return res
