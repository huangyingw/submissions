class Solution(object):
    def reverseList(self, head):
        pre = None
        while head.next:
            temp = head.next
            head.next = pre
            head = temp
            pre = head
        return pre
