_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        palindromes = []
        word_to_index = {}
        for i, word in enumerate(words):
            word_to_index[word] = i
        for i, word in enumerate(words):
            for first_right in range(len(word) + 1):
                left, right = word[:first_right], word[first_right:]
                rev_left, rev_right = left[::-1], right[::-1]
                if first_right != 0 and left == rev_left and rev_right in word_to_index and word_to_index[rev_right] != i:
                    palindromes.append([word_to_index[rev_right], i])
                if right == rev_right and rev_left in word_to_index and word_to_index[rev_left] != i:
                    palindromes.append([i, word_to_index[rev_left]])
        return palindromes
