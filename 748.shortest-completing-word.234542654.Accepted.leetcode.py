import re
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        regex = re.compile('[^a-zA-Z]')
        licensePlate = regex.sub('', licensePlate)
        counter = Counter(licensePlate.lower())
        res = ''
        for word in words:
            if self.contains(counter, word):
                if res == '' or len(word) < len(res):
                    res = word
        return res
    def contains(self, counter1, w2):
        c2 = Counter(w2)
        c2.subtract(counter1)
        return all(map(lambda x: x >= 0, c2.values()))
