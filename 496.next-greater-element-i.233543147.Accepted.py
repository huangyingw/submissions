class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        result = [-1 for _ in range(len(findNums))]
        find_to_i = {}
        for i, num in enumerate(findNums):
            find_to_i[num] = i
        stack = []
        for num in nums:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                if smaller in find_to_i:
                    result[find_to_i[smaller]] = num
            stack.append(num)
        return result
