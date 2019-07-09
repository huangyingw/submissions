_author_ = 'jake'
_project_ = 'leetcode'











class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        node.prev, self.tail.prev.next = self.tail.prev, node
        node.next, self.tail.prev = self.tail, node

    def remove_at_head(self):
        node = self.head.next
        node.next.prev = self.head
        self.head.next = self.head.next.next
        key = node.key
        del node
        return key

    def update(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert(node)


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = DLL()
        self.mapping = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self.queue.update(node)
        return node.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self.queue.update(node)
            return
        node = Node(key, value)
        self.mapping[key] = node
        self.queue.insert(node)
        if self.capacity == 0:
            removed_key = self.queue.remove_at_head()
            del self.mapping[removed_key]
        else:
            self.capacity -= 1
