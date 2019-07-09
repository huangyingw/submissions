_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid
        letters.append(letters[0])
        return letters[left]
