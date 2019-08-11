class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head.next
        fast = head.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
