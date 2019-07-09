_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 > asteroid:
                if stack[-1] == -asteroid:
                    stack.pop()
                    break
                elif stack[-1] > -asteroid:
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)
        return stack
