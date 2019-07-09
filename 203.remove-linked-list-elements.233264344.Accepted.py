_author_ = 'jake'
_project_ = 'leetcode'








class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)
        dummy.next = head
        while head:
            if head.val == val:
                prev.next, head.next, head = head.next, None, head.next
            else:
                prev, head = head, head.next
        return dummy.next
