_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def findMaxLength(self, nums):

        max_len = 0
        balance = 0
        balances = {0: -1}
        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1
            if balance in balances:
                max_len = max(max_len, i - balances[balance])
            else:
                balances[balance] = i
        return max_len
