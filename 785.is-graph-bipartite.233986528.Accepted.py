_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colours = [None] * n
        for i in range(len(graph)):
            if colours[i] is not None:
                continue
            colours[i] = True
            queue = [i]
            while queue:
                v = queue.pop()
                for nbor in graph[v]:
                    if colours[nbor] is None:
                        colours[nbor] = not colours[v]
                        queue.append(nbor)
                    elif colours[nbor] == colours[v]:
                        return False
        return True
