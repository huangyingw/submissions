'''
	Given a binary tree, return the inorder traversal of its nodes' values.
	Example:
	Input: [1,null,2,3]
	   1
	    \
	     2
	    /
	   3
	Output: [1,3,2]
	Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        stack, result = [root], []
        while stack:
            if root.left:
                stack.append(root.left)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                    root = node.right
        return result
