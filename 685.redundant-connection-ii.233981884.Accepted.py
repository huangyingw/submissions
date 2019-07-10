



















class Solution(object):
    def findRedundantDirectedConnection(self, edges):

        n = len(edges)
        parents = [[] for _ in range(n + 1)]
        nbors = [set() for _ in range(n + 1)]
        for a, b in edges:
            parents[b].append(a)
            nbors[a].add(b)
        root = None
        for i, parent in enumerate(parents):
            if len(parent) == 2:
                two_parents = i
            if not parent:
                root = i

        def valid(root):
            visited = set()
            queue = [root]
            while queue:
                node = queue.pop()
                if node in visited:
                    return False
                visited.add(node)
                queue += nbors[node]
            return len(visited) == n
        if root:
            p1, p2 = parents[two_parents]
            nbors[p2].discard(two_parents)
            return [p2, two_parents] if valid(root) else [p1, two_parents]
        for i in range(len(edges) - 1, -1, -1):
            n1, n2 = edges[i]
            nbors[n1].discard(n2)
            if valid(n2):
                return edges[i]
            nbors[n1].add(n2)
