class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        q1 = head
        q2 = head.next
        while q1 != q2:
            if not q2 or not q2.next:
                return False
            q1 = q1.next
            q2 = q2.next.next
        return True
