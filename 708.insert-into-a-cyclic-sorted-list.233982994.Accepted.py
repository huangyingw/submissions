_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            new_node = Node(insertVal, None)
            new_node.next = new_node
            return new_node

        def insert_after(node):
            node.next = Node(insertVal, node.next)
        original_head = head
        while True:
            if head.next.val > head.val:
                if insertVal >= head.val and insertVal <= head.next.val:
                    break
            elif head.next.val < head.val:
                if insertVal >= head.val or insertVal <= head.next.val:
                    break
            elif head.next == original_head:
                break
            head = head.next
        insert_after(head)
        return (original_head)
