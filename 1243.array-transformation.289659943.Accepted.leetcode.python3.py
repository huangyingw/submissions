class Solution(object):
    def transformArray(self, arr):
        changed = True
        while changed:
            new_arr = arr[:]
            changed = False
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                    changed = True
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
                    changed = True
            arr = new_arr
        return arr
