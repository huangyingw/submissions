class Solution(object):
    def __init__(self):
        self.result = []
        self.current = []

    def pathSum(self, root, sum):
        if not root:
            return
        if not root.left and not root.right and root.val == sum:
            self.result.append(list(self.current.append(root.val)))
        self.current.append(root.val)
        self.pathSum(root.left, sum - root.val)
        self.pathSum(root.right, sum - root.val)
        self.current.pop()
        return self.result
