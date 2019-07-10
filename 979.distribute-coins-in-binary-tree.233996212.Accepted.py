










class Solution:
    def distributeCoins(self, root):

        def helper(node, parent):
            if not node:
                return 0
            left = helper(node.left, node)
            right = helper(node.right, node)
            upshift = node.val - 1
            if upshift != 0:
                parent.val += upshift
            node.val = 1
            return left + right + abs(upshift)
        return helper(root, None)
