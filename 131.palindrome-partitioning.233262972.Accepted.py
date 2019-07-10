_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def partition(self, s):

        partitons = []
        self.find_partitions(s, [], partitons)
        return partitons

    def find_partitions(self, s, partial, partitions):
        if not s:
            partitions.append(partial)
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                self.find_partitions(s[i:], partial + [s[:i]], partitions)
