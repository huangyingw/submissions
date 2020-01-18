import itertools


class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        for i1, i2 in itertools.zip_longest(v1, v2, fillvalue=0):
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1
        return 0
