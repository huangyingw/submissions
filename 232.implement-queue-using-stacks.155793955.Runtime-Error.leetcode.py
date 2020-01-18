class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop(-1)

    def peek(self):
        if not self.output:
            while self.input:
                self.append(self.input[-1])
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output
