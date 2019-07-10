'''
	Two elements of a binary search tree (BST) are swapped by mistake.
	Recover the tree without changing its structure.
	Example 1:
	Input: [1,3,null,null,2]
	   1
	  /
	 3
	  \
	   2
	Output: [3,1,null,null,2]
	   3
	  /
	 1
	  \
	   2
'''


class Solution(object):
    def recoverTree(self, root):
        first, second, prev = None, None, None

        def inorder(root):
            if root:
                inorder(root.left)
                if prev is not None and root.val < prev.val:
                    if first is None:
                        first = root
                    else:
                        second = root
                prev = root
                inorder(root.right)
        inorder(root)
        if first and second:
            first.val, second.val = second.val, first.val
