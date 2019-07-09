"""
Problem Link: https://leetcode.com/problems/remove-linked-list-elements/
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""







class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head != None and head.val == val:
            head = head.next
        cur = head
        prev = None
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
