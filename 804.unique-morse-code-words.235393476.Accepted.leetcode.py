class Solution:
    def uniqueMorseRepresentations(self, words):
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        temp = []
        for tmp in words:
            temp.append(''.join([morse_code[ord(n) - 97] for n in tmp]))
        return(len(set(temp)))
