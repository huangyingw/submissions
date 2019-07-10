class Solution(object):
    def lengthOfLongestSubstring(self, s):




        res = 0
        i = 0
        j = 0
        l = len(s)
        myDict = dict()
        while i < l and j < l:
            if myDict.__contains__(s[j]):
                i = max(myDict[s[j]], i)
            res = max(res, j - i + 1)
            myDict[s[j]] = j + 1
            j += 1
        return res
