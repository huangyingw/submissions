

















class MyCircularDeque(object):
    def __init__(self, k):

        self.k = k + 1
        self.q = [None] * self.k
        self.head = self.tail = 0

    def insertFront(self, value):

        if self.isFull():
            return False
        self.head = (self.head + 1) % self.k
        self.q[self.head] = value
        return True

    def insertLast(self, value):

        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail - 1) % self.k
        return True

    def deleteFront(self):

        if self.isEmpty():
            return False
        self.head = (self.head - 1) % self.k
        return True

    def deleteLast(self):

        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.k
        return True

    def getFront(self):

        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self):

        if self.isEmpty():
            return -1
        return self.q[(self.tail + 1) % self.k]

    def isEmpty(self):

        return self.head == self.tail

    def isFull(self):

        return (self.head + 1) % self.k == self.tail
