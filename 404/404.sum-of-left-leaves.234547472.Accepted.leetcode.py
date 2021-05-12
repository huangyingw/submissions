class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

    def sumOfLeftLeaves(self, root):
        sum = 0
        if root != None:
            if root.left != None:
                if root.left.left == None and root.left.right == None:
                    sum += root.left.val
                else:
                    sum += self.sumOfLeftLeaves(root.left)
            if root.right != None:
                sum += self.sumOfLeftLeaves(root.right)
        return sum
