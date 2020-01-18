class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        def helper(i, j):
            if i > j:
                return None
            max_num = float("-inf")
            for k in range(i, j + 1):
                if nums[k] > max_num:
                    max_num = nums[k]
                    max_index = k
            root = TreeNode(max_num)
            root.left = helper(i, max_index - 1)
            root.right = helper(max_index + 1, j)
            return root
        return helper(0, len(nums) - 1)
