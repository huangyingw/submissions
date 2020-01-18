class Solution(object):
    def uniqueMorseRepresentations(self, words):
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse = set()
        for word in words:
            transformation = []
            for c in word:
                transformation.append(codes[ord(c) - ord("a")])
            morse.add("".join(transformation))
        return len(morse)
