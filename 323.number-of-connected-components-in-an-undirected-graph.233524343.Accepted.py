class Solution(object):
    def countComponents(self, n, edges):
        parents = [i for i in range(n)]
        components = n

        def update_parent(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[parents[node]]
            return node
        for a, b, in edges:
            a_parent = update_parent(a)
            b_parent = update_parent(b)
            if a_parent != b_parent:
                parents[a_parent] = b_parent
                components -= 1
        return components
