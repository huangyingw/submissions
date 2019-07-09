_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        outgoing = [set(nbors) for nbors in graph]
        incoming = [[] for _ in range(len(graph))]
        for node, nbors in enumerate(graph):
            for nbor in nbors:
                incoming[nbor].append(node)
        safe = [node for node, nbors in enumerate(outgoing) if not nbors]
        for safe_node in safe:
            nbors = incoming[safe_node]
            for nbor in nbors:
                outgoing[nbor].remove(safe_node)
                if not outgoing[nbor]:
                    safe.append(nbor)
        return [node for node, nbors in enumerate(outgoing) if not nbors]
