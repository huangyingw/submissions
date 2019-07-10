







class Solution(object):
    def sufficientSubset(self, root, limit):

        def reduce_tree(root, limit, curr_sum):
            if not root:
                return None
            l_sum = [curr_sum[0] + root.val]
            r_sum = [l_sum[0]]
            root.left = reduce_tree(root.left, limit, l_sum)
            root.right = reduce_tree(root.right, limit, r_sum)
            curr_sum[0] = max(l_sum[0], r_sum[0])
            if curr_sum[0] < limit:
                root = None
            return root
        curr_sum = [0]
        return reduce_tree(root, limit, curr_sum)
