








from collections import Counter


class Solution(object):
    def originalDigits(self, s):

        digit_freq = [0] * 10
        letter_freq = Counter(s)

        words = [("z", [], 0), ("w", [], 2), ("u", [], 4), ("x", [], 6), ("g", [], 8),
                 ("o", [0, 2, 4], 1), ("r", [0, 4], 3), ("f", [4], 5), ("v", [5], 7), ("i", [5, 6, 8], 9)]
        for letter, other_digits, digit in words:
            word_count = letter_freq[letter]
            for other_digit in other_digits:
                word_count -= digit_freq[other_digit]
            digit_freq[digit] = word_count
        result = []
        for digit, count in enumerate(digit_freq):
            result += [str(digit)] * count
        return "".join(result)
