'''
	Design a data structure that supports all following operations in average O(1) time.
	insert(val): Inserts an item val to the set if not already present.
	remove(val): Removes an item val from the set if present.
	getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
	Example:
	// Init an empty set.
	RandomizedSet randomSet = new RandomizedSet();
	// Inserts 1 to the set. Returns true as 1 was inserted successfully.
	randomSet.insert(1);
	// Returns false as 2 does not exist in the set.
	randomSet.remove(2);
	// Inserts 2 to the set, returns true. Set now contains [1,2].
	randomSet.insert(2);
	// getRandom should return either 1 or 2 randomly.
	randomSet.getRandom();
	// Removes 1 from the set, returns true. Set now contains [2].
	randomSet.remove(1);
	// 2 was already in the set, so return false.
	randomSet.insert(2);
	// Since 2 is the only number in the set, getRandom always return 2.
	randomSet.getRandom();
'''


class RandomizedSet(object):
    def __init__(self):

        self.values = []
        self.positions = {}

    def insert(self, val):

        if val not in self.positions:
            self.values.append(val)
            self.positions[val] = len(self.values) - 1
            return True
        return False

    def remove(self, val):

        if val in self.positions:
            valIdx, lastEle = self.positions[val], self.values[-1]
            self.positions[lastEle], self.values[valIdx] = valIdx, lastEle
            self.values.pop()
            self.positions.pop(val, 0)
            return True
        return False

    def getRandom(self):

        return self.values[random.randint(0, len(self.values) - 1)]
