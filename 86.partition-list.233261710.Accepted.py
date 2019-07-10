








class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):

        lesser_head = lesser = ListNode(None)
        greater_head = greater = ListNode(None)
        node = head
        while node:
            if node.val < x:
                lesser.next = node
                lesser = node
            else:
                greater.next = node
                greater = node
            node = node.next
        greater.next = None
        lesser.next = greater_head.next
        return lesser_head.next
