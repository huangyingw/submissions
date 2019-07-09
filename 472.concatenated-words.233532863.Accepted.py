_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def is_concat(word):
            if not word or word in word_set:
                return True
            for i in range(1, len(word) + 1):
                if word[:i] in word_set and is_concat(word[i:]):
                    return True
            return False
        word_set = set(words)
        results = []
        for word in words:
            for i in range(1, len(word)):
                if word[:i] in word_set and is_concat(word[i:]):
                    results.append(word)
                    break
        return results
