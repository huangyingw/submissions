import heapq
class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False
        if W == 1:
            return True
        hand.sort()
        partials = []
        for num in hand:
            if not partials or partials[0][0] == num:
                heapq.heappush(partials, (num, 1))
                continue
            if num > partials[0][0] + 1:
                return False
            end, length = heapq.heappop(partials)
            if length != W - 1:
                heapq.heappush(partials, (num, length + 1))
        return not partials
