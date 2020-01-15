Morse_tab = [".-", "-...", "-.-.",
             "-..", ".", "..-.", "--.", "....",
             "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.",
             "...", "-", "..-", "...-", ".--",
             "-..-", "-.--", "--.."]


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        if len(words) == 0:
            return 0
        ans_set = set()
        for word in words:
            morsed = ""
            for c in word:
                morsed += Morse_tab[ord(c) - ord('a')]
            ans_set.add(morsed)
        return len(ans_set)
