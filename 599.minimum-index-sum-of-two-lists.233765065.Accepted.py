_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def findRestaurant(self, list1, list2):

        if len(list1) > len(list2):
            list1, list2 = list2, list1
        dict1 = {rest: i for i, rest in enumerate(list1)}
        result = []
        min_sum = float("inf")
        for i, rest in enumerate(list2):
            if i > min_sum:
                break
            if rest not in dict1:
                continue
            sum_i = i + dict1[rest]
            if sum_i < min_sum:
                min_sum = sum_i
                result = [rest]
            elif sum_i == min_sum:
                result.append(rest)
        return result
