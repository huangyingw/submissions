class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow, fast = head.next, head.next.next
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return True
