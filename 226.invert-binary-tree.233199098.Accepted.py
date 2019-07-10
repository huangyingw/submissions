'''
	Invert a binary tree.
	Example:
	Input:
	     4
	   /   \
	  2     7
	 / \   / \
	1   3 6   9
	Output:
	     4
	   /   \
	  7     2
	 / \   / \
	9   6 3   1
'''








class Solution(object):
    def invertTree(self, root):

        if not root:
            return
        leftTree = self.invertTree(root.left)
        rightTree = self.invertTree(root.right)
        root.left = rightTree
        root.right = leftTree
        return root








class Solution(object):
    def invertTree(self, root):

        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
