class Solution(object):
    def reverseList(self, head):
        pre = None

        while pre:
            temp = head.next
            head.next = pre
            pre = head
            head = temp

        return pre
