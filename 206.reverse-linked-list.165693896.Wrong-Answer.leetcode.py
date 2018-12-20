class Solution(object):
    def reverseList(self, head):
        pre = None

        while head:
            temp = head.next
            head.next = pre
            head = temp
            print('head --> %s' % (head.val if head else 'null'))
            pre = head
            print('pre --> %s' % (pre.val if pre else 'null'))

        return pre
