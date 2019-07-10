class Solution(object):
    def largestValues(self, root):
        result = []
        if not root:
            return []
        queue = [root]
        while queue:
            new_queue = []
            max_val = float("-inf")
            for node in queue:
                max_val = max(max_val, node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            result.append(max_val)
            queue = new_queue
        return result
