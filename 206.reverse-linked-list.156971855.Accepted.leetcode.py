class Solution(object):
    def reverseList(self, head):
        pre = None
        temp = head
        while head:
            temp = temp.next
            head.next = pre
            pre = head
            head = temp
        return pre
