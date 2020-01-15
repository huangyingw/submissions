from collections import Counter


class Solution(object):
    def maxScoreWords(self, words, letters, score):
        char_counts = Counter(letters)
        word_scores = []
        a = ord("a")
        for word in words:
            word_scores.append(sum(score[ord(c) - a] for c in word))

        def can_make(word_counts):
            for c, count in word_counts.items():
                if c not in char_counts or char_counts[c] < count:
                    return False
            return True

        def helper(i):
            if i == len(words):
                return 0
            not_use = helper(i + 1)
            word_counts = Counter(words[i])
            if not can_make(word_counts):
                return not_use
            for c, count in word_counts.items():
                char_counts[c] -= count
            use = word_scores[i] + helper(i + 1)
            for c, count in word_counts.items():
                char_counts[c] += count
            return max(use, not_use)
        return helper(0)
