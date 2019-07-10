_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def deleteNode(self, node):

        node.val = node.next.val
        node.next = node.next.next
