class Solution(object):
    def hasCycle(self, head):
        slow, fast = head.next

        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
