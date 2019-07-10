class Solution(object):
    def toGoatLatin(self, S):
        result = []
        for i, word in enumerate(S.split()):
            if word[0] in "aeiouAEIOU":
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            result.append(word + "a" * (i + 1))
        return ' '.join(result)
