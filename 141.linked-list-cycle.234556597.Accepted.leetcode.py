class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
