class Solution(object):
    def reverseOnlyLetters(self, S):
        S = list(S)
        low, high = 0, len(S) - 1
        while low < high:
            if not(S[low].isalpha()):
                low += 1
                continue
            elif not(S[high].isalpha()):
                high -= 1
                continue
            S[low], S[high] = S[high], S[low]
            low += 1
            high -= 1
        return "".join(S)
