_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def reverseVowels(self, s):

        vowels = {"a", "e", "i", "o", "u"}
        vowels |= {c.upper() for c in vowels}
        vowel_i = [i for i, c in enumerate(s) if c in vowels]
        n_vowel = len(vowel_i)
        s = [c for c in s]
        for j in range(n_vowel // 2):
            s[vowel_i[j]], s[vowel_i[n_vowel - j - 1]] = s[vowel_i[n_vowel - j - 1]], s[vowel_i[j]]
        return "".join(s)
