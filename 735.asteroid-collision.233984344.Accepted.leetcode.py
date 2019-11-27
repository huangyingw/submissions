class Solution(object):
    def asteroidCollision(self, asteroids):
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
