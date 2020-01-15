class MyLinkedList(object):
    def __init__(self):
        self.list = []

    def get(self, index):
        if index >= len(self.list):
            return -1
        return self.list[index]

    def addAtHead(self, val):
        self.list = [val] + self.list

    def addAtTail(self, val):
        self.list.append(val)

    def addAtIndex(self, index, val):
        if index > len(self.list):
            return
        self.list.insert(index, val)

    def deleteAtIndex(self, index):
        if index >= len(self.list):
            return
        del self.list[index]
