from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        chars_count = Counter(chars)
        result = 0
        for word in words:
            for c in set(word):
                if word.count(c) > chars_count[c]:
                    break
            else:
                result += len(word)
        return result
