from collections import defaultdict


class Solution(object):
    def generateSentences(self, synonyms, text):
        parents = {}

        def find(s):
            if s not in parents:
                parents[s] = s
            while parents[s] != s:
                s = parents[s]
            return s
        for a, b in synonyms:
            parents[find(a)] = find(b)
        parent_to_synonyms = defaultdict(list)
        for word in parents:
            parent_to_synonyms[find(word)].append(word)
        results = [[""]]
        for word in text.split():
            new_results = []
            synonyms = parent_to_synonyms.get(find(word), [word])
            for synonym in synonyms:
                for result in results:
                    new_results.append(result[:] + [synonym])
            results = new_results
        return [" ".join(result[1:]) for result in sorted(results)]
