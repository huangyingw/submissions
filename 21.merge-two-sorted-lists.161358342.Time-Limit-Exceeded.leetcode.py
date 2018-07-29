class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        nav = dummy

        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                nav.next = l1
            else:
                nav.next = l2
            nav = nav.next

        return dummy.next
