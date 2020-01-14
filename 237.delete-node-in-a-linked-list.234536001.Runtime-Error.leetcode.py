class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
    def deleteNode(self, head, node):
        while head and head.next:
            if head.val == node:
                head = head.next
                return
