class Solution(object):
    def calculateTime(self, keyboard, word):
        char_to_index = {c: i for i, c in enumerate(keyboard)}
        result, index = 0, 0
        for c in word:
            next_index = char_to_index[c]
            result += abs(next_index - index)
            index = next_index
        return result
