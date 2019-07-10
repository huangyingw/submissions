class MaxStack(object):
    def __init__(self):
        self.stack = [(float("-inf"), float("-inf"))]

    def push(self, x):
        self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self):
        x, _ = self.stack.pop()
        return x

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]

    def popMax(self):
        temp = []
        x, target = self.stack.pop()
        while x != target:
            temp.append(x)
            x, _ = self.stack.pop()
        for x in reversed(temp):
            self.push(x)
        return target
