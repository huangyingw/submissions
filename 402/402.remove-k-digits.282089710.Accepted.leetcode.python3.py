class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == num:
            return "0"
        stack = []
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        index = 0
        while index < len(stack) and stack[index] == "0":
            index += 1
        return "0" if index == len(stack) else "".join(stack[index:])
