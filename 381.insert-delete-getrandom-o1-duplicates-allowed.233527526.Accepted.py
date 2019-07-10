_author_ = 'jake'
_project_ = 'leetcode'











from collections import defaultdict
import random


class RandomizedCollection(object):
    def __init__(self):

        self.nums = []
        self.indices = defaultdict(set)

    def insert(self, val):

        result = True
        if val in self.indices:
            result = False
        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)
        return result

    def remove(self, val):

        if val not in self.indices:
            return False
        i = self.indices[val].pop()
        if not self.indices[val]:
            del self.indices[val]
        if i == len(self.nums) - 1:
            self.nums.pop()
        else:
            replacement = self.nums[-1]
            self.nums[i] = replacement
            self.nums.pop()
            self.indices[replacement].discard(len(self.nums))
            self.indices[replacement].add(i)
        return True

    def getRandom(self):

        return self.nums[random.randint(0, len(self.nums) - 1)]
