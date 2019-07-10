class MyHashMap1(object):
    def __init__(self):
        self.table = [-1] * 1000001

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table[key]

    def remove(self, key):
        self.table[key] = -1
