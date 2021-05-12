class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if nums is None or len(nums) == 0:
            return None
        max_index, max_value = 0, 0
        for i, value in enumerate(nums):
            if value >= max_value:
                max_value = value
                max_index = i
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root
