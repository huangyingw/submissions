class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        clone_map = {}
        cur = head
        while cur:
            clone_map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            clone_map.get(cur).next = clone_map.get(cur.next)
            clone_map.get(cur).random = clone_map.get(cur.random)
            cur = cur.next
        return clone_map.get(head)


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            new_node = Node(cur.val)
            cur.next, new_node.next = new_node, cur.next
            cur = new_node.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        dummyHead = Node(0)
        newCur = dummyHead
        while cur:
            newCur.next = cur.next
            cur = cur.next.next
            newCur = newCur.next
        return dummyHead.next
