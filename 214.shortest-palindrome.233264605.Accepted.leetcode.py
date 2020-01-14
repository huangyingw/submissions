class Solution(object):
    def shortestPalindrome(self, s):
        longest_prefix_suffix = self.kmp_table(s + '*' + s[::-1])
        return s[:longest_prefix_suffix:-1] + s
    def kmp_table(self, word):
        failure = [-1] + [0 for _ in range(len(word) - 1)]
        pos = 2
        candidate = 0
        while pos < len(word):
            if word[pos - 1] == word[candidate]:
                failure[pos] = candidate + 1
                candidate += 1
                pos += 1
            elif candidate > 0:
                candidate = failure[candidate]
                failure[pos] = 0
            else:
                failure[pos] = 0
                pos += 1
        return failure[-1]
