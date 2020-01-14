import collections
from functools import reduce
class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]
            return cur.get(END, word)
        return " ".join(map(replace, sentence.split()))
class Solution2:
    def replaceWords(self, dict, sentence):
        from collections import defaultdict
        def init_lookup(dict):
            lookup = defaultdict(list)
            for word in dict:
                lookup[word[0]].append(word)
            return lookup
        lookup = init_lookup(dict)
        new_sentence = []
        words = sentence.split()
        for word in words:
            root = word
            for dict_word in lookup[word[0]]:
                if word.startswith(dict_word) and len(dict_word) < len(root):
                    root = dict_word
            new_sentence.append(root)
        return " ".join(new_sentence)
class Solution3:
    def replaceWords(self, dict, sentence):
        from collections import defaultdict
        root_dict = sorted(dict)
        roots = defaultdict(list)
        for d in root_dict:
            roots[d[0]].append(d)
        words = sentence.split()
        for i in range(len(words)):
            r = words[i]
            if words[i][0] in roots:
                for rr in roots[words[i][0]]:
                    if words[i].startswith(rr) and len(rr) < len(r):
                        r = rr
            words[i] = r
        return " ".join(words)
