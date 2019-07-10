







class Solution(object):
    def removeElements(self, head, val):

        if not head:
            return None
        while head != None and head.val == val:
            head = head.next
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
