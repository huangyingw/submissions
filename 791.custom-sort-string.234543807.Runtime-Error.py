
from collections import Counter


class Solution:






    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        c = Counter(T)
        lefted = c.keys() - set(S)
        return ''.join(letter * c[letter] for letter in ([s for s in S] + [l for l in lefted]))
