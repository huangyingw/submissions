class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        current = None
        while node.next:
            node.val = node.next.val
            current = node
            node = node.next
        current.next = None
