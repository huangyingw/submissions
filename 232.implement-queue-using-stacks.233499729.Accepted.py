












class MyQueue(object):
    def __init__(self):

        self.stack = []
        self.reversed = []
        self.top = None

    def push(self, x):

        if not self.stack:
            self.top = x
        self.stack.append(x)

    def pop(self):

        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()

    def peek(self):

        if self.reversed:
            return self.reversed[-1]
        return self.top

    def empty(self):

        return not self.stack and not self.reversed
