class MyStack(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, x):
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)
    def top(self):
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]
    def empty(self):
        return not self.queue1 and not self.queue2
