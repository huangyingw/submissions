class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
