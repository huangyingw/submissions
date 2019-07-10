













class Solution(object):
    def similarRGB(self, color):

        result = ["
        for i in range(1, 6, 2):
            first, second = int(color[i], 16), int(color[i + 1], 16)
            difference = first - second
            if abs(difference) <= 8:
                char = color[i]
            elif difference > 0:
                char = hex(first - 1)[2]
            else:
                char = hex(first + 1)[2]
            result.append(char * 2)
        return "".join(result)
