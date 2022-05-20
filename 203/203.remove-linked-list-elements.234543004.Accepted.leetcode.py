class Solution:
    def removeElements(self, head, val):

        ret = res = ListNode(0)
        res.next = head
        while res.next:
            if res.next.val == val:
                res.next = res.next.next
            else:
                res = res.next
        return ret.next
