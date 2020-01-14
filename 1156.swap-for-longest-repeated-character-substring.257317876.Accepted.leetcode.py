from collections import defaultdict
class Solution(object):
    def maxRepOpt1(self, text):
        char_substrings = defaultdict(list)
        for i, c in enumerate(text):
            if i == 0 or c != text[i - 1]:
                char_substrings[c].append([i, i])
            else:
                char_substrings[c][-1][1] = i
        result = 0
        for substrings in char_substrings.values():
            for i, (start, end) in enumerate(substrings):
                length = end - start + 1
                result = max(length + int(len(substrings) >= 2), result)
                if i != 0 and substrings[i - 1][1] == start - 2:
                    prev_length = substrings[i - 1][1] - substrings[i - 1][0] + 1
                    result = max(result, length + prev_length + int(len(substrings) >= 3))
        return result
