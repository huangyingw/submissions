'''
	Reverse a linked list from position m to n. Do it in one-pass.
	Note: 1 ≤ m ≤ n ≤ length of list.
	Example:
	Input: 1->2->3->4->5->NULL, m = 2, n = 4
	Output: 1->4->3->2->5->NULL
'''


class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        result = ListNode(0)
        result.next = head
        prev = result
        for index in range(m - 1):
            prev = prev.next
        reverse = None
        curr = prev.next
        for i in range(n - m + 1):
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp
        prev.next.next = curr
        prev.next = reverse
        return result.next
