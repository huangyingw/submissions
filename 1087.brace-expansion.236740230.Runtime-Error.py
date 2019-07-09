


class Solution(object):
    def permute(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return []
        if '{' not in S:
            return [S]
        stack, stack2 = [], []
        brace = 0
        for char in S:
            if char == '{':
                brace = 1
            elif char == '}':
                if not stack:
                    stack = stack2
                else:
                    new_stack = []
                    for char in stack:
                        for char2 in stack2:
                            new_stack.append(char + char2)
                    stack = new_stack
                stack2 = []
                brace = 2
            elif char != ',':
                if brace == 1:
                    stack2.append(char)
                elif brace == 2:
                    stack = [c + char for c in stack]
                    stack2 = []
                else:
                    stack.append(char)
                # print stack
        stack.sort()
        stack.sort(key=len)
        return stack
