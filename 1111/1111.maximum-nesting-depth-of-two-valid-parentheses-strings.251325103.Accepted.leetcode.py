class Solution(object):
    def maxDepthAfterSplit(self, seq):
        result = []
        depth = 0
        for c in seq:
            if c == ")":
                depth -= 1
            result.append(depth % 2)
            if c == "(":
                depth += 1
        return result
