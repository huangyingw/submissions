class Solution(object):
    def maxDistToClosest(self, seats):
        seatsStr = ''.join(str(num) for num in seats)
        maxDistance = 0
        for zeros in re.finditer(r'0+', seatsStr):
            zero = zeros.group(0)
            if zeros.start() == 0:
                maxDistance = len(zero)
            elif zeros.end() == len(seats):
                if maxDistance < len(zero):
                    maxDistance = len(zero)
            elif maxDistance < int((len(zero) + 1) // 2):
                maxDistance = int((len(zero) + 1) // 2)
        return maxDistance
