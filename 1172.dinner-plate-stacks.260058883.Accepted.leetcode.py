import heapq
class DinnerPlates(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.incomplete_stacks = []
    def push(self, val):
        while self.incomplete_stacks:
            i = heapq.heappop(self.incomplete_stacks)
            if i >= len(self.stacks):
                continue
            self.stacks[i].append(val)
            return
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(val)
    def pop(self):
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return val
    def popAtStack(self, index):
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        if index == len(self.stacks) - 1:
            return self.pop()
        heapq.heappush(self.incomplete_stacks, index)
        return self.stacks[index].pop()
