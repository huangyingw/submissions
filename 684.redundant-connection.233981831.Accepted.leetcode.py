class Solution(object):
    def findRedundantConnection(self, edges):
        parents = {}
        def find_parent(n):
            if n not in parents:
                return n
            parents[n] = find_parent(parents[n])
            return parents[n]
        for a, b in edges:
            parent_a, parent_b = find_parent(a), find_parent(b)
            if parent_a == parent_b:
                return [a, b]
            parents[parent_a] = parent_b
