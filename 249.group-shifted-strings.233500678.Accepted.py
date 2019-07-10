_author_ = 'jake'
_project_ = 'leetcode'








from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):

        shifted = defaultdict(list)
        for s in strings:
            shift = ord(s[0]) - ord('a')
            s_shifted = "".join([chr((ord(c) - ord('a') - shift) % 26 + ord('a')) for c in s])
            shifted[s_shifted].append(s)
        return shifted.values()
