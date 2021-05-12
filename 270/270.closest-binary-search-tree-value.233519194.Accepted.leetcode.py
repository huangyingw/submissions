class Solution(object):
    def closestValue(self, root, target):
        closest = root.val
        while root:
            if root.val == target:
                return root.val
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest
