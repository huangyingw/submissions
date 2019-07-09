# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
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
