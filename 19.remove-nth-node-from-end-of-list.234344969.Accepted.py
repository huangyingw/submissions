






class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(0, n + 1):
            if fast:
                fast = fast.next
            else:
                break
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
