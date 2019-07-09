





class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
