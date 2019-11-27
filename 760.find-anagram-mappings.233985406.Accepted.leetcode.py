class Solution(object):
    def anagramMappings(self, A, B):
        B_to_int = {}
        for i, b in enumerate(B):
            B_to_int[b] = i
        result = []
        for a in A:
            result.append(B_to_int[a])
        return result
