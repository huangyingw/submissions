_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nearest_leaves = {0: (float("inf"), 0)}

        def closest_down(node):
            if not node:
                return (float("inf"), 0)
            if not node.left and not node.right:
                result = (0, node.val)
            else:
                left_dist, left_nearest = closest_down(node.left)
                right_dist, right_nearest = closest_down(node.right)
                if left_dist <= right_dist:
                    result = (left_dist + 1, left_nearest)
                else:
                    result = (right_dist + 1, right_nearest)
            nearest_leaves[node.val] = result
            return result

        def closest(node, parent_val):
            if not node:
                return
            if 1 + nearest_leaves[parent_val][0] < nearest_leaves[node.val][0]:
                nearest_leaves[node.val] = (1 + nearest_leaves[parent_val][0], nearest_leaves[parent_val][1])
            closest(node.left, node.val)
            closest(node.right, node.val)
        closest_down(root)
        closest(root, 0)
        return nearest_leaves[k][1]
