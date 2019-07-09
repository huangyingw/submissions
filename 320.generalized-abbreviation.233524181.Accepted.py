_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        abbreviations = [[]]
        for c in word:
            new_abbreviations = []
            for abbr in abbreviations:

                if len(abbr) > 0 and isinstance(abbr[-1], int):
                    new_abbreviations.append(abbr[:-1] + [abbr[-1] + 1])
                else:
                    new_abbreviations.append(abbr + [1])

                new_abbreviations.append(abbr + [c])
            abbreviations = new_abbreviations
        return ["".join(map(str, a)) for a in abbreviations]
