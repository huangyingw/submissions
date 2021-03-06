class Solution(object):
    def findStrobogrammatic(self, n):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8', ]
        if n == 2:
            return ['11', '69', '88', '96']
        result = []
        previous = self.findStrobogrammatic(n - 2)
        for prev in previous:
            result.append('1' + prev + '1')
            result.append('6' + prev + '9')
            result.append('8' + prev + '8')
            result.append('9' + prev + '6')
        return result
