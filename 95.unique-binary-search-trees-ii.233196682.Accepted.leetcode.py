
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def generate(start, end):
            result = []
            if start > end:
                result.append(None)
                return result
            for index in range(start, end + 1):
                left = generate(start, index - 1)
                right = generate(index + 1, end)
                for l in left:
                    for r in right:
                        current = TreeNode(index)
                        current.left = l
                        current.right = r
                        result.append(current)
            return result
        return generate(1, n)
