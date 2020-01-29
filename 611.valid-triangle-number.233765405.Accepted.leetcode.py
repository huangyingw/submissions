from collections import Counter


class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        triangles = 0
        for i, longest_side in enumerate(nums):
            left, right = 0, i - 1
            while left < right:
                shortest_side, middle_side = nums[left], nums[right]
                if shortest_side + middle_side > longest_side:
                    triangles += right - left
                    right -= 1
                else:
                    left += 1
        return triangles
from math import factorial


class Solution2(object):
    def triangleNumber(self, nums):
        sides = Counter(nums)
        if 0 in sides:
            del sides[0]
        sides = list(sides.items())
        sides.sort()
        triangles = 0

        def binom(n, k):
            if k > n:
                return 0
            return factorial(n) // (factorial(n - k) * factorial(k))
        for i, (s1, c1) in enumerate(sides):
            for j, (s2, c2) in enumerate(sides[i:]):
                j2 = j + i
                for s3, c3 in sides[j2:]:
                    if s1 == s2 == s3:
                        triangles += binom(c1, 3)
                    elif s1 == s2:
                        if s1 + s2 > s3:
                            triangles += c3 * binom(c1, 2)
                    elif s2 == s3:
                        triangles += c1 * binom(c2, 2)
                    else:
                        if s1 + s2 > s3:
                            triangles += c1 * c2 * c3
        return triangles
