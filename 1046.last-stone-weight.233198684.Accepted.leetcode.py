class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            max_x = max(stones)
            stones.remove(max_x)
            max_y = max(stones)
            stones.remove(max_y)
            if max_x != max_y:
                stones.append(max_x - max_y)
        return stones[0] if stones else 0
