from collections import defaultdict
class Solution(object):
    def wordsAbbreviation(self, dictionary):
        def make_abbreviation(word, i):
            abbreviation = word[:i + 1] + str(len(word) - (i + 2)) + word[-1]
            return word if len(abbreviation) >= len(word) else abbreviation
        def abbreviate(group, prefix_end):
            new_groups = defaultdict(list)
            for i in group:
                new_groups[dictionary[i][prefix_end]].append(i)
            for new_group in new_groups.values():
                if len(new_group) == 1:
                    abbreviations[new_group[0]] = make_abbreviation(dictionary[new_group[0]], prefix_end)
                else:
                    abbreviate(new_group, prefix_end + 1)
        n = len(dictionary)
        abbreviations = ["" for _ in range(n)]
        groups = defaultdict(list)
        for i, word in enumerate(dictionary):
            groups[make_abbreviation(word, 0)].append(i)
        for abbreviation, group in groups.items():
            if len(group) == 1:
                abbreviations[group[0]] = abbreviation
            else:
                abbreviate(group, 1)
        return abbreviations
