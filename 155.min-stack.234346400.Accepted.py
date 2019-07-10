class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        self.min = min(x, self.min)
        self.stack.append((x, self.min))

    def pop(self):
        if self.stack:
            self.stack.pop()
        self.min = self.stack[-1][1] if self.stack else float('inf')
        return

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.min
