class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while pre:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
