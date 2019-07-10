_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findLongestChain(self, pairs):

        pairs.sort(key=lambda x: x[0])
        chain = 0
        end = pairs[0][0] - 1
        for pair in pairs:
            if end < pair[0]:
                chain += 1
                end = pair[1]
            else:
                end = min(end, pair[1])
        return chain
