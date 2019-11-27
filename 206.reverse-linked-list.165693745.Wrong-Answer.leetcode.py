class Solution(object):
    def reverseList(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            head = temp
            pre = head
        return pre
