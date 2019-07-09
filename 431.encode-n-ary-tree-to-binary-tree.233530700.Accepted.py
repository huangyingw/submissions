_author_ = 'jake'
_project_ = 'leetcode'













class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        binary = TreeNode(root.val)
        if not root.children:
            return binary
        binary.left = self.encode(root.children[0])
        node = binary.left
        for child in root.children[1:]:
            node.right = self.encode(child)
            node = node.right
        return binary

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None
        nary = Node(data.val, [])
        node = data.left
        while node:
            nary.children.append(self.decode(node))
            node = node.right
        return nary
