'''
	Reverse a singly linked list.
	Example:
	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL
'''







class Solution(object):
    def reverseList(self, head):

        if not head:
            return None
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
