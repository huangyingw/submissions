class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
