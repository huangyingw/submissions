class Solution(object):
    def countLetters(self, S):
        previous = "#"
        start = 0
        substrings = 0
        for end, c in enumerate(S):
            if c != previous:
                start = end
                previous = c
            substrings += end - start + 1
        return substrings
