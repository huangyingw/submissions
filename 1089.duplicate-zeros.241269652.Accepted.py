_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def duplicateZeros(self, arr):

        length = 0
        for i, num in enumerate(arr):
            length += 2 if num == 0 else 1
            if length >= len(arr):
                break
        next_fill = len(arr) - 1
        if length > len(arr):
            arr[-1] = 0
            i -= 1
            next_fill -= 1
        for j in range(i, -1, -1):
            arr[next_fill] = arr[j]
            next_fill -= 1
            if arr[j] == 0:
                arr[next_fill] = arr[j]
                next_fill -= 1
