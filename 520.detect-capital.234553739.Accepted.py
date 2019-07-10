

class Solution:
    def detectCapitalUse(self, word):
        if word.islower() or word.isupper() or word.istitle():
            return True
        else:
            return False
