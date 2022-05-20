class Solution(object):
    def reorderList(self, head):
        def split(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            slow.next = None
            return mid

        def reverse(head):
            pre = None
            while head:
                nex = head.next
                head.next = pre
                pre = head
                head = nex
            if pre:
            return pre

        def merge(l1, l2):
            dummy = ListNode(-1)
            nav = dummy
            while l1 and l2:
                nav.next = l1
                l1 = l1.next
                nav = nav.next
                nav.next = l2
                l2 = l2.next
        mid = split(head)
        mid = reverse(mid)
        temp = mid
        while temp:
            temp = temp.next
        merge(head, mid)
