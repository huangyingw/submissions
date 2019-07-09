_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse = set()
        for word in words:
            transformation = []
            for c in word:
                transformation.append(codes[ord(c) - ord("a")])
            morse.add("".join(transformation))
        return len(morse)
