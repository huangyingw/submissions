














class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import heapq


class Solution(object):
    def closestKValues(self, root, target, k):

        closest = [(float('-inf'), 0)]
        self.find_closest(root, target, k, closest)
        return [val for _, val in closest]

    def find_closest(self, node, target, k, closest):
        if not node:
            return
        if abs(node.val - target) < -closest[0][0]:
            heapq.heappush(closest, (-abs(node.val - target), node.val))
            if len(closest) > k:
                heapq.heappop(closest)
            self.find_closest(node.left, target, k, closest)
            self.find_closest(node.right, target, k, closest)
        elif target > node.val:
            self.find_closest(node.right, target, k, closest)
        else:
            self.find_closest(node.left, target, k, closest)
