class Solution(object):
    def reverseList(self, head):
        pre = None

        while head:
            temp = head.next
            head.next = pre
            head = temp
<< << << < Updated upstream
    pre = head
== == == =
    pre = head
>>>>>> > Stashed changes

    return pre
