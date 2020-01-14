from collections import defaultdict
class Solution(object):
    def lastSubstring(self, s):
        n = len(s)
        max_char = max(s)
        candidates = {i for i in range(n) if s[i] == max_char}
        length = 0
        while len(candidates) > 1:
            char_indices = defaultdict(set)
            for i in candidates:
                if i == n - 1:
                    continue
                if i - length - 1 in candidates:
                    continue
                char_indices[s[i + 1]].add(i + 1)
            candidates = char_indices[max(char_indices.keys())]
            length += 1
        return s[candidates.pop() - length:]
