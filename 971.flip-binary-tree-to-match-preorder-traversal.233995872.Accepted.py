_author_ = 'jake'
_project_ = 'leetcode'


















class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        flipped = []
        self.i = 0

        def preorder(node):
            if not node:
                return True
            if voyage[self.i] != node.val:
                return False
            self.i += 1
            if node.left:
                if node.left.val != voyage[self.i]:
                    flipped.append(node.val)
                    node.left, node.right = node.right, node.left
                if not preorder(node.left):
                    return False
            return preorder(node.right)
        return flipped if preorder(root) else [-1]
