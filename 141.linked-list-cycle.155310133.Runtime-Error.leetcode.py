





class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow, fast = head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
