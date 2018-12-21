class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None

        node.val = node.next.val
        node.next = node.next.next
