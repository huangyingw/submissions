class Solution:
    def getMinimumDifference(self, root):
        stack = [root]
        queue = []
        while stack and stack[0]:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
            else:
                queue.append(top.val)
                stack.pop(-1)
                if top.right:
                    stack.append(top.right)
                    top.right = None
        res = queue[-1] - queue[0]
        for i in range(1, len(queue)):
            res = min(res, queue[i] - queue[i - 1])
        return res
class Solution2:
    def getMinimumDifference(self, root):
        iot_list = []
        def InOrderTraversal(node):
            if node.left:
                InOrderTraversal(node.left)
            iot_list.append(node.val)
            if node.right:
                InOrderTraversal(node.right)
            return
        InOrderTraversal(root)
        min_abs = float('inf')
        for i in range(1, len(iot_list)):
            diff = iot_list[i] - iot_list[i - 1]
            if diff < min_abs:
                min_abs = diff
        return min_abs
