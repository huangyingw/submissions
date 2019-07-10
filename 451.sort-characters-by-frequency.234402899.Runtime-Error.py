
from collections import Counter


class Solution:

    def frequencySort1(self, s):
        mapping = sorted(((idx, v) for idx, v in Counter(s).items()), key=lambda item: item[1], reverse=True)
        return "".join([idx * v for (idx, v) in mapping])

    def frequencySort2(self, s):
        c = Counter(s).most_common(len(s))
        return ''.join([i[1] * i[0] for i in c])
