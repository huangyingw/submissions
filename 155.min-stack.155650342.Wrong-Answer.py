class MinStack(object):
    def __init__(self):

        self.data = []
        self.min = []

    def push(self, x):

        self.data.append(x)
        if not self.min or self.min[-1] <= x:
            self.min.append(x)

    def pop(self):

        temp = self.data.pop()
        if temp == self.min[-1]:
            self.min.pop(-1)

    def top(self):

        return self.data[-1]

    def getMin(self):

        return self.min[-1]
