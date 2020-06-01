class MovingAverage(object):
    def __init__(self, size):
        self.array = [None for _ in range(size)]
        self.idx = 0
        self.total = 0

    def next(self, val):
        if self.array[self.idx]:
            self.total -= self.array[self.idx]
        self.total += val
        self.array[self.idx] = val
        self.idx = (self.idx + 1) % len(self.array)
        count = len(self.array)
        if not self.array[-1]:
            count = self.idx
        return self.total // float(count)
