'''
	Given a linked list, remove the n-th node from the end of list and return its head.
	Example:
	Given linked list: 1->2->3->4->5, and n = 2.
	After removing the second node from the end, the linked list becomes 1->2->3->5.
'''







class Solution(object):
    def removeNthFromEnd(self, head, n):

        if not head:
            return None
        ref = head
        while n > 0:
            ref = ref.next
            n -= 1
        if ref is None:
            return head.next
        else:
            main = head
            while ref.next:
                main = main.next
                ref = ref.next
            main.next = main.next.next
            return head
