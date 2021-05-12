class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        elif root.left == None and root.right == None:
            if sum == root.val:
                return True
            else:
                return False
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum(self, root, sum):
        if root is None:
            return False
        stack = [(root, sum)]
        while stack:
            node, _sum = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                return True
            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))
        return False
