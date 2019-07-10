



class Solution:
    def diStringMatch(self, S):

        length = len(S)
        ans = []
        left = 0
        right = length
        for i in S:
            if i == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans
