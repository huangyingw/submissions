

class Solution:
    def uniqueMorseRepresentations(self, words):
        letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        new = set()
        for i in words:
            s = ""
            for w in i:
                s += letters[ord(w) - 97]
            new.add(s)
        return len(new)
