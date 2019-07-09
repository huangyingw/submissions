_author_ = 'jake'
_project_ = 'leetcode'








class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        prev = dummy = ListNode(None)
        next_nodes = [(l.val, l) for l in lists if l]
        heapq.heapify(next_nodes)
        while next_nodes:
            value, node = heapq.heappop(next_nodes)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(next_nodes, (node.next.val, node.next))
        return dummy.next
