class Solution(object):
    def heightChecker(self, heights):
        s = sorted(heights)
        count = 0
        for i, h in enumerate(heights):
            if h != s[i]:
                count += 1
        return count
