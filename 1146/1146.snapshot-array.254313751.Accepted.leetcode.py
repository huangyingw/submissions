import bisect


class SnapshotArray(object):
    def __init__(self, length):
        self.history = [[[-1, 0]] for _ in range(length)]
        self.id = 0

    def set(self, index, val):
        if val == self.history[index][-1][1]:
            return
        if self.history[index][-1][0] == self.id:
            self.history[index][-1][1] = val
            return
        self.history[index].append([self.id, val])

    def snap(self):
        self.id += 1
        return self.id - 1

    def get(self, index, snap_id):
        i = bisect.bisect_left(self.history[index], [snap_id, float("inf")])
        return self.history[index][i - 1][1]
