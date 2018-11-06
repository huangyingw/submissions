class MaxStack(object):
    def __init__(self):
        self.data = []
        self.max = []

    def push(self, x):
        self.data.append(x)

        if not self.max or self.max[-1] <= x:
            self.max.append(x)

    def pop(self):
        temp = self.data.pop()

        if temp == self.max[-1]:
            self.max.pop(-1)

        return temp

    def top(self):
        return self.data[-1]

    def peekMax(self):
        return self.max[-1]

    def popMax(self):
        max = self.peekMax()
        buffer = []

        while self.top() != max:
            buffer.append(self.pop())

        self.pop()

        while buffer:
            self.push(buffer.pop())

        return max
