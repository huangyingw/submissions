class Solution(object):
    def anagramMappings(self, A, B):

        val_index = {}
        ans = []
        for i, n in enumerate(B):
            val_index[n] = i
        for n in A:
            ans.append(val_index[n])
        return ans
