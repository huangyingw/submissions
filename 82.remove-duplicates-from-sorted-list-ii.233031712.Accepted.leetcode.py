
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        result = ListNode(0)
        ans = result
        curr = head
        while curr:
            value = curr.val
            count = 0
            while curr and curr.val == value:
                curr = curr.next
                count += 1
            if count == 1:
                result.next = ListNode(value)
                result = result.next
        return ans.next
