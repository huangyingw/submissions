















class Solution(object):
    def recoverFromPreorder(self, S):

        self.i = 0

        def helper(required_depth):
            depth = 0
            while self.i + depth < len(S) and S[self.i + depth] == "-":
                depth += 1
            if depth != required_depth:
                return None
            self.i += depth
            val = 0
            while self.i < len(S) and S[self.i] != "-":
                val = val * 10 + int(S[self.i])
                self.i += 1
            node = TreeNode(val)
            node.left = helper(required_depth + 1)
            node.right = helper(required_depth + 1)
            return node
        return helper(0)
