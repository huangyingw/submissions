_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def helper(left, right, same):
            if left > right:
                return 0
            if (left, right, same) in memo:
                return memo[(left, right, same)]

            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                same += 1
            result = helper(left, right - 1, 0) + (same + 1) ** 2
            for i in range(left, right):

                if boxes[i] == boxes[right]:
                    result = max(result, helper(i + 1, right - 1, 0) + helper(left, i, same + 1))
            memo[(left, right, same)] = result
            return result
        memo = {}
        return helper(0, len(boxes) - 1, 0)
