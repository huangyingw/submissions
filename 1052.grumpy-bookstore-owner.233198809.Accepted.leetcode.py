


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        result = 0
        prefix_sum = [0] * (len(customers) + 1)
        index = 0
        for customer, grump in zip(customers, grumpy):
            prefix_sum[index + 1] = prefix_sum[index]
            if grump == 0:
                result += customer
            else:
                prefix_sum[index + 1] += customer
            index += 1
        # print prefix_sum
        curr_max = result + prefix_sum[X]
        # print curr_max
        for index in range(X + 1, len(prefix_sum)):
            temp_max = result + prefix_sum[index] - prefix_sum[index - X]
            # print temp_max
            curr_max = max(curr_max, temp_max)
        return curr_max
