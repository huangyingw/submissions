_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def can_ship(capacity):
            days = D
            load = 0
            for weight in weights:
                if weight + load > capacity:
                    days -= 1
                    load = 0
                load += weight
                if days == 0:
                    return False
            return True
        min_capacity = max(weights)
        max_capacity = sum(weights)
        while min_capacity < max_capacity:
            mid_capacity = (min_capacity + max_capacity) // 2
            if can_ship(mid_capacity):
                max_capacity = mid_capacity
            else:
                min_capacity = mid_capacity + 1
        return min_capacity
