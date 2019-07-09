_author_ = 'jake'
_project_ = 'leetcode'












import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}
        self.items = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mapping:
            self.items.append(val)
            self.mapping[val] = len(self.items) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mapping:
            return False
        index = self.mapping[val]
        self.items[index] = self.items[-1]
        self.mapping[self.items[index]] = index
        self.items.pop()
        del self.mapping[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        return self.items[random.randint(0, len(self.items) - 1)]
