class Solution(object):
    def canMakePaliQueries(self, s, queries):
        char_odd_bits = [0]
        for c in s:
            char_odd_bits.append(char_odd_bits[-1] ^ (1 << ord(c) - ord("a")))
        result = []
        for left, right, k in queries:
            left_odd_bits = char_odd_bits[left]
            right_odd_bits = char_odd_bits[right + 1]
            odd_chars = bin(left_odd_bits ^ right_odd_bits).count("1")
            odd_chars -= (right - left + 1) % 2
            odd_chars -= 2 * k
            result.append(odd_chars <= 0)
        return result
