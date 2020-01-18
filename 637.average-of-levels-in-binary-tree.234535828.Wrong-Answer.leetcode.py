class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        res = []
        lis = [root]
        while lis:
            lis2 = []
            level_sum = 0
            for each in lis:
                level_sum += each.val
                if each.left:
                    lis2.append(each.left)
                if each.right:
                    lis2.append(each.right)
            res.append(level_sum / len(lis))
            lis = lis2
        return res
