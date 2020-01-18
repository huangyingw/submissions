class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.i = 0

    def str2tree(self, s):
        def next_num():
            num, neg = 0, False
            if s[self.i] == "-":
                neg = True
                self.i += 1
            while self.i < len(s) and s[self.i] not in {"(", ")"}:
                num = num * 10 + int(s[self.i])
                self.i += 1
            return TreeNode(-num) if neg else TreeNode(num)

        def helper():
            if self.i >= len(s):
                return None
            root = next_num()
            if self.i < len(s) and s[self.i] == "(":
                self.i += 1
                root.left = helper()
                self.i += 1
            if self.i < len(s) and s[self.i] == "(":
                self.i += 1
                root.right = helper()
                self.i += 1
            return root
        return helper()
