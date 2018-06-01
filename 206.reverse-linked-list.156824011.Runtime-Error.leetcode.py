class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            if not head or not head.next:
                return
            second = head.next
            helper(second)
            second.next = head
            return second

        result = helper(head)
        head.next = None
        return result
