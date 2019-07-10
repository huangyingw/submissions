
class Solution:


    def findWords(self, words):

        line1 = "qwertyuiopQWERTYUIOP"
        line2 = "asdfghjklASDFGHJKL"
        line3 = "zxcvbnmZXCVBNM"
        res = []
        for word in words:
            s = set(word)
            if s.issubset(line1) or s.issubset(line2) or s.issubset(line3):
                res.append(word)
        return res
