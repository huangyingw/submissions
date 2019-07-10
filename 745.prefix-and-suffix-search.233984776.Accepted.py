class WordFilter(object):
    def __init__(self, words):
        self.prefix_root = [set(), [None for _ in range(26)]]
        self.suffix_root = [set(), [None for _ in range(26)]]
        self.weights = {}

        def insert(word, forwards):
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]
            node[0].add(word)
            for c in iterate_word:
                if not node[1][ord(c) - ord("a")]:
                    node[1][ord(c) - ord("a")] = [set(), [None for _ in range(26)]]
                node = node[1][ord(c) - ord("a")]
                node[0].add(word)
        for weight, word in enumerate(words):
            self.weights[word] = weight
            insert(word, True)
            insert(word, False)

    def f(self, prefix, suffix):
        def find_words(word, forwards):
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]
            for c in iterate_word:
                node = node[1][ord(c) - ord("a")]
                if not node:
                    return -1
            return node[0]
        prefix_matches = find_words(prefix, True)
        suffix_matches = find_words(suffix, False)
        if prefix_matches == -1 or suffix_matches == -1:
            return -1
        matches = prefix_matches & suffix_matches
        weight = -1
        for match in matches:
            weight = max(weight, self.weights[match])
        return weight
