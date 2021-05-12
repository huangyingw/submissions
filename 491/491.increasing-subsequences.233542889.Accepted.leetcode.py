class Solution(object):
    def findSubsequences(self, nums):
        subsequences = set()
        for num in nums:
            new_subsequences = set()
            new_subsequences.add((num,))
            for s in subsequences:
                if num >= s[-1]:
                    new_subsequences.add(s + (num,))
            subsequences |= new_subsequences
        return [s for s in subsequences if len(s) > 1]
