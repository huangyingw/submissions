class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        current = prev.next.next

        while prev and current:
            prev.next.next = current.next
            current.next = prev.next
            prev.next = current
            prev = prev.next.next
            current = prev.next.next

        return dummy.next
