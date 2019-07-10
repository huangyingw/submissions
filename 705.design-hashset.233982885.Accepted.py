











class MyHashSet(object):
    def __init__(self):

        self.size = 10000
        self.hashset = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def add(self, key):

        if not self.contains(key):
            self.hashset[self.hash_function(key)].append(key)

    def remove(self, key):

        if self.contains(key):
            self.hashset[self.hash_function(key)].remove(key)

    def contains(self, key):

        return key in self.hashset[self.hash_function(key)]
