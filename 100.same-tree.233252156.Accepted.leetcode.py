class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                if not node1 == node2:
                    return False
        return True
