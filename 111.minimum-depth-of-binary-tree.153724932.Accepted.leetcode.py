class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return depth
