_author_ = 'jake'
_project_ = 'leetcode'












class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashset = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            self.hashset[self.hash_function(key)].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            self.hashset[self.hash_function(key)].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset[self.hash_function(key)]
