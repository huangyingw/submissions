from collections import defaultdict


class MapSum(object):
    def __init__(self):
        self.dict = defaultdict(int)
        self.words = defaultdict(int)

    def insert(self, key, val):
        if key in self.words:
            self.words[key], val = val, val - self.words[key]
        else:
            self.words[key] = val
        for i in range(len(key)):
            prefix = key[:i + 1]
            self.dict[prefix] += val

    def sum(self, prefix):
        return self.dict[prefix]
