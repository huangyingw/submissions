_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def readBinaryWatch(self, num):

        if num == 0:
            return ["0:00"]
        bits_set = [[i] for i in range(10)]
        for max_bit in range(10 - num + 1, 10):
            new_bits_set = []
            for time in bits_set:
                for bit in range(time[-1] + 1, max_bit + 1):
                    new_bits_set.append(time + [bit])
            bits_set = new_bits_set
        result = []
        for time in bits_set:
            hours, mins = 0, 0
            for bit in time:
                if bit >= 6:
                    hours += 1 << (bit - 6)
                else:
                    mins += 1 << bit
            if hours < 12 and mins < 60:
                mins = str(mins)
                if len(mins) == 1:
                    mins = "0" + mins
                result.append(str(hours) + ":" + mins)
        return result
