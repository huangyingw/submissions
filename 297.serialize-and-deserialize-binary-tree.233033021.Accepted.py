'''
	Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
	Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
	Example:
	You may serialize the following tree:
	    1
	   / \
	  2   3
	     / \
	    4   5
	as "[1,2,3,null,null,4,5]"
'''


class Codec:
    def serialize(self, root):
        def preorder(root):
            if root:
                seralizeTree.append(str(root.val) + ',')
                preorder(root.left)
                preorder(root.right)
            else:
                seralizeTree.append('
                                    seralizeTree=[]
                                    preorder(root)
                                    return ''.join(seralizeTree)
                                    def deserialize(self, data):
                                    def buildTree(preorder):
                                    value=preorder.pop(0)
                                    if value == '
                                    return None
                                    node=TreeNode(int(value))
                                    node.left=buildTree(preorder)
                                    node.right=buildTree(preorder)
                                    return node
                                    preorder=data.split(',')[:-1]
                                    return buildTree(preorder)
