class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        split_node, prev, curr = None, None, head
        count = 1
        while count <= m and curr is not None:
            if count == m:
                split_node = prev
            prev = curr
            curr = curr.next
            count += 1
        tail, next_node = prev, None
        while curr is not None and count <= n:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            count += 1
        if split_node is not None:
            split_node.next = prev
        if tail is not None:
            tail.next = curr
        if m == 1:
            return prev
        return head
