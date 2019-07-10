_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def flatten(self, head):

        node = head
        while node:
            if node.child:
                old_next = node.next
                node.next = self.flatten(node.child)
                node.next.prev = node
                node.child = None
                while node.next:
                    node = node.next
                node.next = old_next
                if old_next:
                    old_next.prev = node
            node = node.next
        return head
