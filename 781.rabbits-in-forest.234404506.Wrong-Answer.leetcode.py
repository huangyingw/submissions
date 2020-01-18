class Solution:
    def numRabbits(self, answers):
        from collections import Counter
        mapping = Counter(answers)
        ret = 0
        for idx, val in mapping.items():
            ret += val if val % (idx + 1) == 0 else (val // (idx + 1) + 1) * (idx + 1)
        return ret

    def numRabbits(self, answers):
        from collections import Counter
        dic = Counter(answers)
        return sum([math.ceil(dic[i] / (i + 1)) * (i + 1) for i in dic.keys()])
