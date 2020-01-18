class Solution(object):
    def toGoatLatin(self, S):
        S = S.split()
        vowels = {"a", "e", "i", "o", "u"}
        for i, word in enumerate(S):
            if word[0].lower() not in vowels:
                S[i] = S[i][1:] + S[i][0]
            S[i] += "ma" + "a" * (i + 1)
        return " ".join(S)
