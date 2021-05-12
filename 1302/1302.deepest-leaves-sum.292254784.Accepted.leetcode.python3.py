class Solution(object):
    def deepestLeavesSum(self, root):
        nodes = [root]
        while nodes:
            level_sum = 0
            new_nodes = []
            for node in nodes:
                level_sum += node.val
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return level_sum
