
















from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):

        bulls, cows = 0, 0
        unmatched_secret, unmatched_guess = defaultdict(int), defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                unmatched_secret[s] += 1
                unmatched_guess[g] += 1
        for g, count in unmatched_guess.items():
            cows += min(unmatched_secret[g], count)
        return str(bulls) + "A" + str(cows) + "B"
