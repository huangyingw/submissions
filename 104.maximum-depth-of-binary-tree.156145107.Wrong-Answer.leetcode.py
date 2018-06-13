class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0

        queue = [root]
        depth = 0

        while len(queue) > 0:
            depth += 1
            size = len(queue)

            for i in range(size):
                node = queue.pop()

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)
        return depth
