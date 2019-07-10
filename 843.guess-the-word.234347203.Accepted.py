









from collections import defaultdict


class Solution:
    def findSecretWord(self, wordlist, master):

        def compPair(x, y):
            return sum(c1 == c2 for c1, c2 in zip(x, y))

        def mostOverlapWord():
            count = [defaultdict(lambda: 0) for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    count[i][c] += 1
            return max(candidates, key=lambda x: sum(count[i][c] for i, c in enumerate(x)))
        candidates = wordlist[:]
        while candidates:
            word = mostOverlapWord()
            match = master.guess(word)
            if match == 6:
                return
            candidates = [w for w in candidates if compPair(word, w) == match]
