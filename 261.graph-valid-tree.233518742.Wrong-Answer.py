_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        class Solution(object):
            def validTree(self, n, edges):
                """
                :type n: int
                :type edges: List[List[int]]
                :rtype: bool
                """
                def dfs(node):
                    nbors = adjacency.pop(node, [])
                    for nbor in nbors:
                        dfs(nbor)
                if len(edges) != n - 1:
                    return False
                adjacency = {i: [] for i in range(n)}
                for a, b in edges:
                    adjacency[a].append(b)
                    adjacency[b].append(a)
                dfs(0)
                return not adjacency


class Solution2(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def find(node):
            if parents[node] == -1:
                return node
            return find(parents[node])
        if len(edges) != n - 1:
            return False
        parents = [-1] * n
        for a, b in edges:
            a_parent = find(a)
            b_parent = find(b)
            if a_parent == b_parent:
                return False
            parents[a_parent] = b_parent
        return True
