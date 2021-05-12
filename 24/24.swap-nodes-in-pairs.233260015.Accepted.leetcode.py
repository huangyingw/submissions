class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        prev = dummy = ListNode(None)
        while head and head.next:
            next_head = head.next.next
            prev.next = head.next
            head.next.next = head
            prev = head
            head = next_head
        prev.next = head
        return dummy.next
