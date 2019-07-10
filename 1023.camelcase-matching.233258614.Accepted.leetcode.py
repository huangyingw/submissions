_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def camelMatch(self, queries, pattern):

        def can_match(query):
            i = 0
            for c in pattern:
                while i < len(query) and c != query[i]:
                    if query[i].isupper():
                        return False
                    i += 1
                if i == len(query):
                    return False
                i += 1
            return query[i:] == query[i:].lower()
        return [can_match(query) for query in queries]
