_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict


class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(int)
        self.words = defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.words:
            self.words[key], val = val, val - self.words[key]
        else:
            self.words[key] = val
        for i in range(len(key)):
            prefix = key[:i + 1]
            self.dict[prefix] += val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.dict[prefix]
