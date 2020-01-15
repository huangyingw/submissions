from collections import Counter
class Solution:
    def repeatedNTimes1(self, A):
        mapping = Counter(A)
        return mapping.most_common(1)[0][0]
    def repeatedNTimes2(self, A):
        lookup = set()
        for element in A:
            if element not in lookup:
                lookup.add(element)
            else:
                return element
    def repeatedNTimes3(self, A):
        import random
        i = 0
        j = 0
        while (A[i] != A[j] or i == j):
            i = random.randint(0, len(A) - 1)
            j = random.randint(0, len(A) - 1)
        return A[i]
