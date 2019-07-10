






class Solution(object):
    def averageOfLevels(self, root):

        nodes = [root]
        result = []
        while True:
            row_sum, row_count = 0, 0
            new_nodes = []
            for node in nodes:
                if not node:
                    continue
                row_sum += node.val
                row_count += 1
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            if row_count == 0:
                break
            result.append(row_sum / float(row_count))
            nodes = new_nodes
        return result
