_author_ = 'jake'
_project_ = 'leetcode'










class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.smaller = 0
        self.left = None
        self.right = None


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = [0 for _ in range(len(nums))]
        if len(nums) < 2:
            return smaller
        root = TreeNode(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            node = root
            count = 0
            while True:
                if nums[i] < node.val:
                    node.smaller += 1
                    if not node.left:
                        node.left = TreeNode(nums[i])
                        break
                    else:
                        node = node.left
                else:
                    count += node.smaller
                    if nums[i] > node.val:
                        count += 1
                    if not node.right:
                        node.right = TreeNode(nums[i])
                        break
                    else:
                        node = node.right
            smaller[i] = count
        return smaller
