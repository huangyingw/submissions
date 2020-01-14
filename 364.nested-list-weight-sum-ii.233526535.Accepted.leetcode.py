class Solution(object):
    def depthSumInverse(self, nestedList):
        depth_sums = []
        for nested in nestedList:
            self.dfs(nested, 0, depth_sums)
        total = 0
        max_depth = len(depth_sums)
        for i, depth_sum in enumerate(depth_sums):
            total += (max_depth - i) * depth_sum
        return total
    def dfs(self, nested, depth, depth_sums):
        if len(depth_sums) <= depth:
            depth_sums.append(0)
        if nested.isInteger():
            depth_sums[depth] += nested.getInteger()
        else:
            for n in nested.getList():
                self.dfs(n, depth + 1, depth_sums)
class Solution2(object):
    def depthSumInverse(self, nestedList):
        unweighted, weighted = 0, 0
        q = nestedList
        while q:
            new_q = []
            for nested in q:
                if nested.isInteger():
                    unweighted += nested.getInteger()
                else:
                    new_q += nested.getList()
            q = new_q
            weighted += unweighted
        return weighted
