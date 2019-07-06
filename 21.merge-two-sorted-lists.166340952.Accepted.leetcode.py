class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        current = dummy
        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        return dummy.next
