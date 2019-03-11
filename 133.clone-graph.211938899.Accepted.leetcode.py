class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        queue = []
        neighbor_to_copy = {}
        newHead = Node(node.val, [])
        queue.append(node)
        neighbor_to_copy[node] = newHead

        while queue:
            curr = queue.pop()
            currNeighbors = curr.neighbors

            for aNeighbor in currNeighbors:
                if aNeighbor not in neighbor_to_copy:
                    copy = Node(aNeighbor.val, [])
                    neighbor_to_copy[aNeighbor] = copy
                    queue.append(aNeighbor)

                neighbor_to_copy[curr].neighbors.append(neighbor_to_copy[aNeighbor])

        return newHead
