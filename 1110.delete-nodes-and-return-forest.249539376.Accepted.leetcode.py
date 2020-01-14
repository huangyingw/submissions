class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        result = []
        def helper(node, has_parent):
            if not node:
                return None
            delete = node.val in to_delete
            if not has_parent and not delete:
                result.append(node)
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return None if delete else node
        helper(root, False)
        return result
