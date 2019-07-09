
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        if head:
            slow = head  # the mover
            while slow:
                group = []
                while slow and len(group) < k:
                    group.append(slow)
                    slow = slow.next
                    if not slow and len(group) < k:
                        return head
                for i in range(k / 2):
                    print i, k - i - 1
                    group[i].val, group[k - i - 1].val = group[k - i - 1].val, group[i].val
        return head
# Space: O(k)
# Time: O(N)
