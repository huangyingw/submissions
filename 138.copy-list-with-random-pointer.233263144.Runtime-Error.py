_author_ = 'jake'
_project_ = 'leetcode'










class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = head
        while node:
            next = node.next
            copy = RandomListNode(node.label)
            node.next = copy
            copy.next = next
            node = next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        pseudo = prev = RandomListNode(0)
        node = head
        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next
        return pseudo.next
