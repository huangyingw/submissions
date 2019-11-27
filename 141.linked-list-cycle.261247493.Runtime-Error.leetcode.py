class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
