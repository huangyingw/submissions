class Solution(object):
    def preorder(self, root):
        result = []
        if root == None:
            return result
        stack = [root]
        while len(stack) != 0:
            cur = stack.pop()
            result.append(cur.val)
            stack.extend(reversed(cur.children))
        return result


class Solution(object):
    def preorder(self, root):
        if root == None:
            return []
        lst = [root.val]
        for node in root.children:
            lst += self.preorder(node)
        return lst
