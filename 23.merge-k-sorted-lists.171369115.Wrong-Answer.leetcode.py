class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        nav = dummy

        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                nav.next = l1
                l1 = l1.next
            else:
                nav.next = l2
                l2 = l2.next

            nav = nav.next

        return dummy.next

    def mergeKLists(self, lists):
        dummy = ListNode(-1)

        for li in lists:
            dummy = self.mergeTwoLists(dummy, li)

        return dummy.next
