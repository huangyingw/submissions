from collections import Counter
class Solution(object):
    def generatePalindromes(self, s):
        char_counts = Counter(s)
        odd_char = ""
        for char, count in char_counts.items():
            if count % 2 != 0:
                if odd_char:
                    return []
                odd_char = char
                char_counts[odd_char] -= 1
        palindromes = []
        self.build_palindromes(palindromes, [], char_counts, len(s) // 2)
        return ["".join(p + [odd_char] + p[::-1]) for p in palindromes]
    def build_palindromes(self, palindromes, partial, char_counts, remaining):
        if remaining == 0:
            palindromes.append(partial[:])
        for c in char_counts.keys():
            if char_counts[c] == 0:
                continue
            char_counts[c] -= 2
            partial.append(c)
            self.build_palindromes(palindromes, partial, char_counts, remaining - 1)
            partial.pop()
            char_counts[c] += 2
