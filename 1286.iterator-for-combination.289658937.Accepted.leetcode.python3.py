class CombinationIterator(object):
    def __init__(self, characters, combinationLength):
        self.chars = characters
        self.combination = list(range(combinationLength))
        self.combination[-1] -= 1
        n = len(characters)
        self.final = list(range(n - combinationLength, n))
    def next(self):
        i = len(self.combination) - 1
        while self.combination[i] == self.final[i]:
            i -= 1
        self.combination[i] += 1
        for j in range(i + 1, len(self.combination)):
            self.combination[j] = self.combination[j - 1] + 1
        return "".join(self.chars[i] for i in self.combination)
    def hasNext(self):
        return self.combination != self.final
