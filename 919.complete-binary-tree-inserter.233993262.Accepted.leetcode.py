class CBTInserter:
    def __init__(self, root):
        self.nodelist = [root]
        for node in self.nodelist:
            if node.left:
                self.nodelist.append(node.left)
            if node.right:
                self.nodelist.append(node.right)
    def insert(self, v):
        node = TreeNode(v)
        self.nodelist.append(node)
        n = len(self.nodelist)
        parent = self.nodelist[(n // 2) - 1]
        if n % 2 == 0:
            parent.left = node
        else:
            parent.right = node
        return parent.val
    def get_root(self):
        return self.nodelist[0]
