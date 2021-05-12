class Solutions:
    def search(self, reader, target):
        low = 0
        high = 1
        while reader.get(high) < target:
            low = high + 1
            high *= 2
        while low <= high:
            mid = (low + high) // 2
            num = reader.get(mid)
            if num == target:
                return mid
            if num > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
