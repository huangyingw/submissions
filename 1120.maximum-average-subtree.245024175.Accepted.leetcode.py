class Solution(object):
    def maximumAverageSubtree(self, root):
        self.result = 0

        def helper(node):
            if not node:
                return 0, 0
            left_nodes, left_sum = helper(node.left)
            right_nodes, right_sum = helper(node.right)
            total_nodes = 1 + left_nodes + right_nodes
            total_sum = node.val + left_sum + right_sum
            self.result = max(self.result, total_sum / float(total_nodes))
            return total_nodes, total_sum
        helper(root)
        return self.result
