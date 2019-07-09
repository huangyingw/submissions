class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        q = collections.deque([0])
        while q:
            curr = q.popleft()
            visited[curr] = True
            for node in neighbors[curr]:
                if node not in visited:
                    visited[node] = True
                    q.append(node)
        return len(visited) == n
