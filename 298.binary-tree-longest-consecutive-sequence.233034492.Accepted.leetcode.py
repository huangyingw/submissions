







class Solution(object):
    def longestConsecutive(self, root):

        return self.longestConsecutive_helper(root, -10000, 1)

    def longestConsecutive_helper(self, root, previous, curr):

        if root is None:
            return 0
        if root.val - 1 == previous:
            curr += 1
        else:
            curr = 1
        l_res = self.longestConsecutive_helper(root.left, root.val, curr)
        r_res = self.longestConsecutive_helper(root.right, root.val, curr)
        return max(curr, l_res, r_res)
