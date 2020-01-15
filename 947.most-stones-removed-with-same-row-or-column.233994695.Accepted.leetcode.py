class Solution:
    def removeStones(self, stones):
        parents = {}

        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x

        def union(x, y):
            parents.setdefault(x, x)
            parents.setdefault(y, y)
            parents[find(x)] = find(y)
        for i, j in stones:
            union(i, ~j)
        return len(stones) - len({find(x) for x in parents})
