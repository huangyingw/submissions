class Solution(object):
    def minMutation(self, start, end, bank):
        chars = set("ACGT")
        bank = set(bank)
        if end not in bank:
            return -1
        distance = 0
        frontier = [start]
        while frontier:
            new_frontier = []
            distance += 1
            for gene in frontier:
                for i in range(len(gene)):
                    for c in chars:
                        if c == gene[i]:
                            continue
                        mutation = list(gene)
                        mutation[i] = c
                        mutation = "".join(mutation)
                        if mutation == end:
                            return distance
                        if mutation in bank:
                            bank.discard(mutation)
                            new_frontier.append(mutation)
            frontier = new_frontier
        return -1
