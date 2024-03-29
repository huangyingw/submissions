class Solution(object):
    def levelOrderBottom(self, root):
        queue = [root]
        result = []
        while queue and root:
            current = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                current.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.insert(0, current)
        return result
