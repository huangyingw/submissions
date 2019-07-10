













class Solution(object):


    def minAbbreviation(self, target, dictionary):
        def abbr(target, num):
            word, count = [], 0
            for w in target:
                if num & 1 == 1:
                    if count:
                        word += str(count)
                        count = 0
                    word.append(w)
                else:
                    count += 1
                num >>= 1
            if count:
                word.append(str(count))
            return "".join(word)
        m = len(target)
        diffs = []
        for word in dictionary:
            if len(word) != m:
                continue
            bits = 0
            for i, char in enumerate(word):
                if char != target[i]:
                    bits += 2 ** i
            diffs.append(bits)
        if not diffs:
            return str(m)
        min_abbr = target
        for i in range(2 ** m):
            if all(d & i for d in diffs):
                abbr_i = abbr(target, i)
                if len(abbr_i) < len(min_abbr):
                    min_abbr = abbr_i
        return min_abbr
