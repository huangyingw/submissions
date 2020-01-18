class Solution(object):
    def minCut(self, s):
        min_cuts = [i - 1 for i in range(len(s) + 1)]
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1
        return min_cuts[-1]
