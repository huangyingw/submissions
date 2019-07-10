





















class MyCircularQueue(object):
    def __init__(self, k):

        self.k = k + 1
        self.q = [None] * self.k
        self.head = self.tail = 0

    def enQueue(self, value):

        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail - 1) % self.k
        return True

    def deQueue(self):

        if self.isEmpty():
            return False
        self.head = (self.head - 1) % self.k
        return True

    def Front(self):

        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):

        if self.isEmpty():
            return -1
        return self.q[(self.tail + 1) % self.k]

    def isEmpty(self):

        return self.head == self.tail

    def isFull(self):

        return (self.head + 1) % self.k == self.tail
