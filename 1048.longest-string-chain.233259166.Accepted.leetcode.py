from collections import defaultdict
class Solution(object):
    def longestStrChain(self, words):
        longest = defaultdict(int)
        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = longest[word[:i] + word[i + 1:]]
                longest[word] = max(longest[word], prev + 1)
        return max(longest.values())
