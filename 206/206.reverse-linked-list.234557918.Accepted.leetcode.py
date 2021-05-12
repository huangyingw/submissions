class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    """ 
    -------- Recursive Solution --------
    def reverseList(self, head, prev = None):
        if not head:
            return prev
        cur, head.next = head.next, prev
        return self.reverseList(cur,head)
    """
