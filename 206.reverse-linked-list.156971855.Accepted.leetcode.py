class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        temp = head
        while head:
            temp = temp.next
            head.next = pre
            pre = head
            head = temp
        return pre
