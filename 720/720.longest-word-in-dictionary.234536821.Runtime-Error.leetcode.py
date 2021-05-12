from collections import defaultdict


class Solution(object):
    def longestWord1(self, words):
        seen, res = set(""), ""
        buckets = defaultdict(list)
        min_len, max_len = float('inf'), float('-inf')
        for idx, w in enumerate(words):
            buckets[len(w)].append(idx)
            min_len, max_len = min(min_len, len(w)), max(max_len, len(w))
        for l in range(min_len, max_len + 1):
            for idx in buckets[l]:
                w = words[idx]
                if w[:-1] in seen:
                    seen.add(w)
                    if len(w) > len(res) or (len(w) == len(res) and res > w):
                        res = w
        return res

    def longestWord2(self, words):
        max_len = 0
        ans = ""
        words.sort(key=lambda x: len(x))
        D = {}
        for w in words:
            if len(w) == 1 or w[:-1] in D:
                D[w] = 1
                if len(w) > max_len:
                    ans = w
                    max_len = len(w)
                if w < ans:
                    ans = w
        return ans
