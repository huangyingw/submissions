_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        rotations = [0 for _ in range(n)]
        for i, num in enumerate(A):
            min_rot = (i + 1) % n
            max_rot = (n - num + i + 1) % n
            rotations[min_rot] += 1
            rotations[max_rot] -= 1
            if min_rot > max_rot:
                rotations[0] += 1
        score, max_score, best_rotation = 0, 0, 0
        for i, r in enumerate(rotations):
            score += r
            if score > max_score:
                max_score = score
                best_rotation = i
        return best_rotation
