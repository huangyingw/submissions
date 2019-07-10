class Solution(object):
    def removeNthFromEnd(self, head, n):
        p1, p2 = head, head
        if not head:
            return head
        for i in range(n):
            p1 = p1.next
        if not p1:
            return p2.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head
