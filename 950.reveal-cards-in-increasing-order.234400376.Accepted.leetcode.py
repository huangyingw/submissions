from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = deque(range(N))
        ans = [None] * N
        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ans
