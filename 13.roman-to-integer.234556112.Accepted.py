class Solution(object):
    def romanToInt(self, s):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = prev = dic[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            val = dic[s[i]]
            if val < prev:
                num -= val
            else:
                num += val
            prev = val
        return num
