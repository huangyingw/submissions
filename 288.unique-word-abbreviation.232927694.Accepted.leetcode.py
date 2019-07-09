class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.dic = {}
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]

            self.dic[abb] = word if abb not in self.dic else "" if self.dic[abb] != word else self.dic[abb]




    def isUnique(self, word):
        abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abb not in self.dic or self.dic[abb] == word
