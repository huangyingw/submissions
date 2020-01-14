from collections import Counter
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        return [i for i, count in Counter(arr1 + arr2 + arr3).items() if count == 3]
