_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def minCameraCover(self, root):

        covered = {None}

        def helper(node, parent):
            if not node:
                return 0
            result = helper(node.left, node) + helper(node.right, node)
            if node.left not in covered or node.right not in covered:
                covered.update({parent, node, node.left, node.right})
                result += 1
            return result
        cameras = helper(root, None)
        return cameras if root in covered else cameras + 1
