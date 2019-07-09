








class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        lis = [root]
        while lis:
            lis2 = []
            level = []
            for each in lis:
                if each.left:
                    lis2.append(each.left)
                if each.right:
                    lis2.append(each.right)
                level.append(each.val)
            res.append(level)
            lis = lis2
        return res[::-1]
