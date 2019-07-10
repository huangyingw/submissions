_author_ = 'jake'
_project_ = 'leetcode'
















class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):

        node, count = root, 0
        while node:
            count += 1
            node = node.next
        part_length, odd_parts = divmod(count, k)
        result = []
        prev, node = None, root
        for _ in range(k):
            required = part_length
            if odd_parts > 0:
                odd_parts -= 1
                required += 1
            result.append(node)
            for _ in range(required):
                prev, node = node, node.next
            if prev:
                prev.next = None
        return result
