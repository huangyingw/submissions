_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def candy(self, ratings):

        left = [1 for _ in range(len(ratings))]
        right = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        candies = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            candies += max(left[i], right[i])
        return candies
