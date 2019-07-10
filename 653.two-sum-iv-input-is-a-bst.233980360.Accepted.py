









class Solution(object):
    def findTarget(self, root, k):

        visited = set()

        def traverse(node):
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return traverse(node.left) or traverse(node.right)
        return traverse(root)
