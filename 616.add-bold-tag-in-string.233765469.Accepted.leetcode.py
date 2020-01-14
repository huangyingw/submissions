from collections import defaultdict
class Solution(object):
    def addBoldTag(self, s, dict):
        in_tag = [False for _ in range(len(s))]
        start_letters = defaultdict(list)
        for word in dict:
            start_letters[word[0]].append(word)
        matches = []
        for i, c in enumerate(s):
            new_matches = []
            for word, word_index in matches:
                if c == word[word_index + 1]:
                    if word_index + 1 == len(word) - 1:
                        for j in range(i - len(word) + 1, i + 1):
                            in_tag[j] = True
                    else:
                        new_matches.append([word, word_index + 1])
            for word in start_letters[c]:
                if len(word) == 1:
                    in_tag[i] = True
                else:
                    new_matches.append([word, 0])
            matches = new_matches
        result = []
        for i, c in enumerate(s):
            if in_tag[i] and (i == 0 or not in_tag[i - 1]):
                result.append("<b>")
            elif not in_tag[i] and (i != 0 and in_tag[i - 1]):
                result.append("</b>")
            result.append(c)
        if in_tag[-1]:
            result.append("</b>")
        return "".join(result)
