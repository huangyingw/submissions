class Solution(object):
    def boldWords(self, words, S):
        S = "#" + S + "#"
        bold = [False for _ in range(len(S))]
        for word in words:
            i = S.find(word, 1)
            while i != -1:
                bold[i:i + len(word)] = [True] * len(word)
                i = S.find(word, i + 1)
        result = []
        for i in range(len(S)):
            if bold[i] and not bold[i - 1]:
                result.append("<b>")
            elif not bold[i] and bold[i - 1]:
                result.append("</b>")
            result.append(S[i])
        result = result[1:-1]
        return "".join(result)
