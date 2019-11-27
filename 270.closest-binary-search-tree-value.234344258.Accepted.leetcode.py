class Solution:
    def closestValue(self, root, target):
        result = root.val
        while root:
            result = min((root.val, result), key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return result

    def closestValue(self, root, target):
        child = root.left if root.val > target else root.right
        if not child:
            return root.val
        child_val = self.closestValue(child, target)
        return min((root.val, child_val), key=lambda x: abs(x - target))
