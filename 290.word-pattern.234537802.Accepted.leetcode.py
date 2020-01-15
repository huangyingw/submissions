class Solution:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
