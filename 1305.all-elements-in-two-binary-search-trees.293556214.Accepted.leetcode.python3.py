class Solution(object):
    def getAllElements(self, root1, root2):
        def inorder(node, ascending):
            if not node:
                return
            inorder(node.left, ascending)
            ascending.append(node.val)
            inorder(node.right, ascending)
        tree1, tree2 = [], []
        inorder(root1, tree1)
        inorder(root2, tree2)
        result = []
        i, j = 0, 0
        while i < len(tree1) and j < len(tree2):
            if tree1[i] <= tree2[j]:
                result.append(tree1[i])
                i += 1
            else:
                result.append(tree2[j])
                j += 1
        return result + tree1[i:] + tree2[j:]
