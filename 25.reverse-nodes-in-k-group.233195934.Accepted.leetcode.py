class Solution(object):
    def reverseKGroup(self, head, k):
        if head:
            slow = head
            while slow:
                group = []
                while slow and len(group) < k:
                    group.append(slow)
                    slow = slow.next
                    if not slow and len(group) < k:
                        return head
                for i in range(k // 2):
                    group[i].val, group[k - i - 1].val = group[k - i - 1].val, group[i].val
        return head
