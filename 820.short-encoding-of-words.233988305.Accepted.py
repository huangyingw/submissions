_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        required = set(words)
        for word in words:
            for i in range(1, len(word) - 1):
                required.discard(word[i:])
        return sum(len(w) for w in required) + len(required)
