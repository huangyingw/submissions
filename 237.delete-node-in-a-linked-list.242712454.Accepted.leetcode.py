class Solution(object):
    def deleteNode(self, node):
        if not node.next:
            node = None
        pre = None
        while node.next:
            node.val = node.next.val
            pre = node
            node = node.next
        pre.next = None
