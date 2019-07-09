







class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root:
                seralizeTree.append(str(root.val) + ',')
                preorder(root.left)
                preorder(root.right)
            else:
                seralizeTree.append('
        seralizeTree = []
        preorder(root)
        return ''.join(seralizeTree)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(preorder):
            value = preorder.pop(0)
            if value == '
                return None
            node = TreeNode(int(value))
            node.left = buildTree(preorder)
            node.right = buildTree(preorder)
            return node
        preorder = data.split(',')[:-1]
        return buildTree(preorder)
