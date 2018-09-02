class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while prev:
            current = prev.next.next
            prev.next.next = current.next
            current.next = prev.next
            prev.next = current
            prev = prev.next.next

        return dummy.next
