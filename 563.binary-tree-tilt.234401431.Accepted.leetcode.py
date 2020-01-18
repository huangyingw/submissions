class Solution(object):
    def findTilt(self, root):
        self.ans = 0

        def _sum(node):
            if not node:
                return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.ans
