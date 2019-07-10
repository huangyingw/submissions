class Solution(object):
    def depthSum(self, nestedList):
        return self.depthSum_helper(nestedList, 1)

    def depthSum_helper(self, nestedList, depth):
        res = 0
        for l in nestedList:
            if l.isInteger():
                res += l.getInteger() * depth
            else:
                res += self.depthSum_helper(l.getList(), depth + 1)
        return res
