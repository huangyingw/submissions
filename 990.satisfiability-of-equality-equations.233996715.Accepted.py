_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def equationsPossible(self, equations):

        graph = [[] for _ in range(26)]
        not_equal = []
        for eqn in equations:
            first, op, second = eqn[0], eqn[1], eqn[3]
            first, second = ord(first) - ord("a"), ord(second) - ord("a")
            if op == "=":
                graph[first].append(second)
                graph[second].append(first)
            else:
                not_equal.append((first, second))
        groups = [None] * 26

        def dfs(node, group):
            if groups[node] is None:
                groups[node] = group
                for nbor in graph[node]:
                    dfs(nbor, group)
        for i in range(26):
            dfs(i, i)
        for first, second in not_equal:
            if groups[first] == groups[second]:
                return False
        return True
