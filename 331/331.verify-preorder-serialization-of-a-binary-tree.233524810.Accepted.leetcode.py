class Solution(object):
    def isValidSerialization(self, preorder):
        if not preorder:
            return True
        expected_leaves = 1
        for node in preorder.split(","):
            if expected_leaves == 0:
                return False
            if node == "#":
                expected_leaves -= 1
            else:
                expected_leaves += 1
        return expected_leaves == 0
