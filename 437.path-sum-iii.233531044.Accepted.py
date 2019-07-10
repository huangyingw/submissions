









from collections import defaultdict


class Solution(object):
    def pathSum(self, root, sum):

        paths = defaultdict(int)
        paths[0] = 1

        def helper(node, partial):
            if not node:
                return 0
            partial += node.val
            count = paths[partial - sum]
            paths[partial] += 1
            count += helper(node.left, partial)
            count += helper(node.right, partial)
            paths[partial] -= 1
            return count
        return helper(root, 0)
