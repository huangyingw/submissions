"""
Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""







class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """













        if head is None or head.next is None:
            return head
        nextHead = head.next.next
        newHead = head.next
        head.next.next = head
        head.next = self.swapPairs(nextHead)
        return newHead
