_author_ = 'jake'
_project_ = 'leetcode'




























from re import sub


class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def replace_vowels(word):
            return sub('[aeiou]', '_', word)
        wordsset = set(wordlist)
        lower_words, vowel_words = {}, {}
        for word in wordlist:
            lower_words.setdefault(word.lower(), word)
        for word in lower_words.keys():
            replaced = replace_vowels(word)
            vowel_words.setdefault(replaced, lower_words[word])

        def check(word):
            if word in wordsset:
                return word
            low = word.lower()
            result = lower_words.get(low, "")
            if result == "":
                replaced = replace_vowels(low)
                result = vowel_words.get(replaced, "")
            return result
        return [check(query) for query in queries]
