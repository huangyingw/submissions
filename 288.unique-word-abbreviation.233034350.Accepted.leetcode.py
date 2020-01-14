class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.dictionary = set(dictionary)
        self.abb_dic = {}
        for s in self.dictionary:
            curr = self.getAbb(s)
            if curr in self.abb_dic:
                self.abb_dic[curr] = False
            else:
                self.abb_dic[curr] = True
    def isUnique(self, word):
        abb = self.getAbb(word)
        hasAbbr = self.abb_dic.get(abb, None)
        return hasAbbr == None or (hasAbbr and word in self.dictionary)
    def getAbb(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
