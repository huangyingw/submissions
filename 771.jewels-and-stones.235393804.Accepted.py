class Solution:
    def numJewelsInStones(self, J, S):
        return (len(re.split(''.join([str(n) + '|' for n in J]), S)) - 1)
