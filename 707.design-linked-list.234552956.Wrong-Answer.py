


class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class MyLinkedList(object):
    def __init__(self):

        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):

        if index >= self.length or index < 0:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):

        temp = Node(val)
        if not self.head:
            self.head = temp
            self.tail = self.head
        else:
            temp.next = self.head
            self.head = temp
        self.length += 1

    def addAtTail(self, val):

        temp = Node(val)
        if not self.tail:
            self.tail = temp
            self.head = self.tail
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def addAtIndex(self, index, val):

        if index > self.length or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            temp = Node(val)
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            temp.next = cur.next
            cur.next = temp
            self.length += 1

    def deleteHead(self):
        if not self.head:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1

    def deleteTail(self):
        if not self.tail:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None
            self.tail = cur
        self.length -= 1

    def deleteAtIndex(self, index):

        if index >= self.length:
            return
        if index == 0:
            self.deleteHead()
        elif index == self.length - 1:
            self.deleteTail()
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            self.length -= 1
