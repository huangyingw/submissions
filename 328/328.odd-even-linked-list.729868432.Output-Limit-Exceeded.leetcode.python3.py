class Solution(object):
    def oddEvenList(self, head):
        even_head = even = ListNode(None)
        odd_head = odd = ListNode(None)
        while head:
            odd.next = head
            odd = odd.next
            if head.next:
                even.next = head.next
            even = even.next
            if head.next:
                head = head.next.next
        odd.next = even_head.next
        return odd_head.next
