class MyHashMap(object):
    def __init__(self):
        self.size = 10000
        self.nodes = [None] * self.size

    def put(self, key, value):
        index = hash(key) % self.size
        if self.nodes[index] is None:
            self.nodes[index] = ListNode(-1, -1)
        prev = find(self.nodes[index], key)
        if prev.next is None:
            prev.next = ListNode(key, value)
        else:
            prev.next.val = value

    def get(self, key):
        index = hash(key) % self.size
        if self.nodes[index] is None:
            return -1
        prev = find(self.nodes[index], key)
        if prev.next is None:
            return -1
        else:
            return prev.next.val

    def remove(self, key):
        index = hash(key) % self.size
        if self.nodes[index] is None:
            return
        prev = find(self.nodes[index], key)
        if prev.next is None:
            return
        prev.next = prev.next.next


def find(bucket, key):
    node = bucket
    prev = None
    while node is not None and node.key != key:
        prev = node
        node = node.next
    return prev


class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
