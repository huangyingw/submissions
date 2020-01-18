class Solution:
    def compareVersion(self, version1, version2):
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        for i in range(max(len(v1), len(v2))):
            vv1 = v1[i] if i < len(v1) else 0
            vv2 = v2[i] if i < len(v2) else 0
            if vv1 > vv2:
                return 1
            elif vv1 < vv2:
                return -1
        return 0


class Solution:
    def compareVersion(self, version1, version2):
        if version1 == version2:
            return 0
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        for i, j in itertools.zip_longest(v1, v2, fillvalue=0):
            if i < j:
                return -1
            elif i > j:
                return 1
        return 0
