class Solution(object):
    def alienOrder(self, words):
        nodes, ancestors = sets.Set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            self.findEdges(words[i - 1], words[i], ancestors)
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""
        return "".join(result)

    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))

    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            result.append(node)
        elif visited[node] == root:
            return True
        return False
