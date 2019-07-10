'''
	Given a binary tree, determine if it is a valid binary search tree (BST).
	Assume a BST is defined as follows:
	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.
'''








class Solution(object):
    def isValidBST(self, root):

        if not root:
            return True
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        previous = result[0]
        for index in range(1, len(result)):
            if previous >= result[index]:
                return False
            previous = result[index]
        return True
