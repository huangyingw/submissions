'''
	Given a linked list, swap every two adjacent nodes and return its head.
	Example:
	Given 1->2->3->4, you should return the list as 2->1->4->3.
'''







class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        ref = head
        while ref is not None and ref.next is not None:
            ref.val, ref.next.val = ref.next.val, ref.val
            ref = ref.next.next
        return head
