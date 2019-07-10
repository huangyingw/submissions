_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def indexPairs(self, text, words):

        result = []
        for word in words:
            i = -1
            while True:
                i = text.find(word, i + 1)
                if i == -1:
                    break
                result.append([i, i + len(word) - 1])
        return sorted(result)
