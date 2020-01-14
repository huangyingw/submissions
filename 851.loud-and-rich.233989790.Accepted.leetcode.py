class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        richer_than = [set() for _ in range(n)]
        for a, b in richer:
            richer_than[b].add(a)
        result = [None] * n
        def update_results(person):
            if result[person] is not None:
                return
            result[person] = person
            for rich in richer_than[person]:
                update_results(rich)
                if quiet[result[rich]] < quiet[result[person]]:
                    result[person] = result[rich]
        for i in range(n):
            update_results(i)
        return result
