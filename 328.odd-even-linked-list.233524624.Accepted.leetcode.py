class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            head = head.next.next if even else None
        odd.next = even_head.next
        return odd_head.next
