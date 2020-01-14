class Solution(object):
    def maxDepth(self, root):
        q, level = root and [root], 0
        while q:
            q, level = [child for node in q for child in node.children if child], level + 1
        return level
    def maxDepth(self, root, level=1):
        return max(root and [self.maxDepth(child, level + 1) for child in root.children] + [level] or [0])
