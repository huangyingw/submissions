from collections import defaultdict
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        substrings = defaultdict(int)
        letters = defaultdict(int)
        for end in range(len(s)):
            letters[s[end]] += 1
            start = end - minSize + 1
            if start >= 0:
                if len(letters) <= maxLetters:
                    substrings[s[start:end + 1]] += 1
                letters[s[start]] -= 1
                if letters[s[start]] == 0:
                    del letters[s[start]]
        return 0 if not substrings else max(substrings.values())
