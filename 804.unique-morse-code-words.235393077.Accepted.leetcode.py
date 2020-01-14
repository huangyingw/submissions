class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MorseCodeDic = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.."}
        AnserSet = set()
        for word in words:
            word2morse = ""
            for alphabet in word:
                word2morse += MorseCodeDic[alphabet]
            AnserSet.add(word2morse)
        return len(AnserSet)
