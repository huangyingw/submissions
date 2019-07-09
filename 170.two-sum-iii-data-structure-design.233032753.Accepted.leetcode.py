class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.value_count = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.value_count:
            self.value_count[number] += 1
        else:
            self.value_count[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for val in self.value_count:
            diff = value - val
            if diff in self.value_count and (diff != val or self.value_count[val] > 1):
                return True
        return False
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
