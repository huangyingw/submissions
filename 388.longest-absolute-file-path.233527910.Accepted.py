_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def lengthLongestPath(self, input):

        longest = 0
        depths = [0]
        for line in input.splitlines():
            stripped = line.lstrip("\t")
            depth = len(line) - len(stripped)
            if "." in line:
                longest = max(longest, len(stripped) + depth + depths[depth])
            else:
                if len(depths) <= depth + 1:
                    depths.append(0)
                depths[depth + 1] = depths[depth] + len(stripped)
        return longest
