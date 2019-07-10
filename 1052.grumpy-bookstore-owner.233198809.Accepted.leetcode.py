class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):

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

        curr_max = result + prefix_sum[X]

        for index in range(X + 1, len(prefix_sum)):
            temp_max = result + prefix_sum[index] - prefix_sum[index - X]

            curr_max = max(curr_max, temp_max)
        return curr_max
