class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        high, low = sum(weights) + 1, max(weights)
        while(low < high):
            mid = (high + low) / 2
            temp_left = mid
            packet_at_left = D - 1
            for weight in weights:
                if weight <= mid:
                    if temp_left < weight:
                        if packet_at_left == 0:
                            low = mid + 1
                            break
                        packet_at_left -= 1
                        temp_left = mid - weight
                    else:
                        temp_left -= weight
            else:
                high = mid
        return low


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)
        while left < right:
            curr_sum, groups, invalid = 0, 0, True
            mid = left + ((right - left) >> 1)
            for weight in weights:
                if weight > mid:
                    invalid = False
                    break
                if curr_sum + weight > mid:
                    groups += 1
                    curr_sum = 0
                curr_sum += weight
            if invalid and groups < D:
                right = mid
            else:
                left = mid + 1
        return left
