from collections import Counter
from itertools import combinations
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        def word_to_int(s):
            bits = 0
            for c in s:
                bits |= (1 << (ord(c) - ord("a")))
            return bits
        word_bits_counter = Counter(word_to_int(w) for w in words)
        result = []
        for puzzle in puzzles:
            first_char_bit = word_to_int(puzzle[0])
            other_char_bits = [word_to_int(c) for c in puzzle[1:]]
            valid = 0
            for k in range(7):
                for combination in combinations(other_char_bits, k):
                    valid += word_bits_counter[first_char_bit + sum(combination)]
            result.append(valid)
        return result
