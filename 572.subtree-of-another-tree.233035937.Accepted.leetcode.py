







class Solution(object):

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_res = self.preorder(s, True)
        t_res = self.preorder(t, True)
        return t_res in s_res

    def preorder(self, root, isLeft):
        if root is None:
            if isLeft:
                return "lnull"
            else:
                return "rnull"
        return "
