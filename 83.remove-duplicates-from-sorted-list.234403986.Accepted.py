







class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        root, tail, head = head, head, head.next
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return root
