_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
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
