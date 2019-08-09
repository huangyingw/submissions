class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            if fast == slow:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
