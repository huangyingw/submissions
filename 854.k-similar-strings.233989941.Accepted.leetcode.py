class Solution(object):
    def kSimilarity(self, A, B):
        visited = set()
        k = 0
        frontier = {A}
        while True:
            if B in frontier:
                return k
            new_frontier = set()
            for word in frontier:
                if word in visited:
                    continue
                i = 0
                while word[i] == B[i]:
                    i += 1
                for j in range(i + 1, len(A)):
                    if word[j] != B[i]:
                        continue
                    swapped = word[:i] + word[j] + word[i + 1:j] + word[i] + word[j + 1:]
                    new_frontier.add(swapped)
            k += 1
            visited |= frontier
            frontier = new_frontier
