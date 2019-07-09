_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        results = []

        def nodes_at_distance(node, distance):
            if not node:
                return
            if distance == 0:
                results.append(node.val)
            else:
                nodes_at_distance(node.left, distance - 1)
                nodes_at_distance(node.right, distance - 1)

        def helper(node):
            if not node:
                return -1
            if node == target:
                nodes_at_distance(node, K)
                return 0
            left, right = helper(node.left), helper(node.right)
            if left == -1 and right == -1:
                return -1
            distance_to_target = 1 + max(left, right)
            if K - distance_to_target == 0:
                nodes_at_distance(node, 0)
            elif K - distance_to_target > 0:
                other_side = node.left if left == -1 else node.right
                nodes_at_distance(other_side, K - distance_to_target - 1)
            return distance_to_target
        helper(root)
        return results
