class MovingAverage(object):
    def __init__(self, size):
        self.array = [None for _ in range(size)]
        self.i = 0
        self.total = 0

    def next(self, val):
        if self.array[self.i] is not None:
            self.total -= self.array[self.i]
        self.total += val
        self.array[self.i] = val
        self.i = (self.i + 1) % len(self.array)
        count = len(self.array)
        if self.array[-1] is None:
            count = self.i
        return self.total // float(count)
