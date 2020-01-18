class Solution(object):
    def removeVowels(self, S):
        vowels = set("aeiou")
        return "".join(c for c in S if c not in vowels)
