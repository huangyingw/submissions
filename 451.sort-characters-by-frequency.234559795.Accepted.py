class Solution(object):
    def frequencySort(self, s):

        sSet = set(s)
        sTable = []

        for key in sSet:
            Count = s.count(key)
            sTable.append((Count, key * Count))

        sTable.sort(key=lambda table: table[0], reverse=True)
        return ''.join(map(lambda table: table[1], sTable))
