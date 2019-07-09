_author_ = 'jake'
_project_ = 'leetcode'












class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashmap = [[] for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, index = self.key_index(key)
        if index == -1:
            self.hashmap[bucket].append([key, value])
        else:
            self.hashmap[bucket][index][1] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, index = self.key_index(key)
        return -1 if index == -1 else self.hashmap[bucket][index][1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, index = self.key_index(key)
        if index != -1:
            del self.hashmap[bucket][index]

    def hash_function(self, key):
        return key % self.size

    def key_index(self, key):
        bucket = self.hash_function(key)
        pairs = self.hashmap[bucket]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                return (bucket, i)
        return (bucket, -1)
