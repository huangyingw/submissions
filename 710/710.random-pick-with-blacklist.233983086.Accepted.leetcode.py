from random import randint


class Solution(object):
    def __init__(self, N, blacklist):
        self.white = N - len(blacklist)
        blacklist = set(blacklist)
        self.white_to_move = [i for i in range(self.white, N) if i not in blacklist]
        self.mapping = {b: self.white_to_move.pop() for b in blacklist if b < self.white}

    def pick(self):
        rand = randint(0, self.white - 1)
        return self.mapping[rand] if rand in self.mapping else rand
