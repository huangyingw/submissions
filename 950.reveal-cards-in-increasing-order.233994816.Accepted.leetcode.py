from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        index = deque(range(n))
        result = [None] * n
        for card in sorted(deck):
            result[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return result
