











class Solution(object):
    def findContentChildren(self, g, s):

        content = 0
        child = 0
        g.sort()
        s.sort()
        for cookie in s:
            if child == len(g):
                break
            if g[child] <= cookie:
                content += 1
                child += 1
        return content
