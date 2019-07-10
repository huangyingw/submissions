







class Solution(object):
    def partition(self, head, x):

        headLess, headGreater = ListNode(0), ListNode(0)
        cur1, cur2 = headLess, headGreater
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur2.next = None
        cur1.next = headGreater.next
        return headLess.next
