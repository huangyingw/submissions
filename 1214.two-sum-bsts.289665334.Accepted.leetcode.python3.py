class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        seen = set()
        def explore(node):
            if not node:
                return
            seen.add(node.val)
            explore(node.left)
            explore(node.right)
        explore(root1)
        def find(node):
            if not node:
                return False
            if target - node.val in seen:
                return True
            return find(node.left) or find(node.right)
        return find(root2)
