class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList)
                return
            for start in range(index, len(candidates)):
                recursive(candidates, target - candidates[start], currList + [candidates[start]], start)
        recursive(candidates, target, [], 0)
        return result
