











class Solution(object):
    def minimumLengthEncoding(self, words):

        required = set(words)
        for word in words:
            for i in range(1, len(word) - 1):
                required.discard(word[i:])
        return sum(len(w) for w in required) + len(required)
