from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        letters = [c.lower() for c in licensePlate if c > "9"]
        freq = Counter(letters)
        words.sort(key=lambda x: len(x))
        for word in words:
            if len(word) < len(letters):
                continue
            word_freq = Counter(word)
            for c, count in freq.items():
                if c not in word_freq or word_freq[c] < count:
                    break
            else:
                return word
