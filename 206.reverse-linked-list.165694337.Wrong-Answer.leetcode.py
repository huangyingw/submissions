class Solution(object):
    def reverseList(self, head):
        if not head:
            return head
        prev = None
        while head.next:
            temp = head.next
            head.next = prev
            head = temp
            prev = head
        return prev
