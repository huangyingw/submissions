import collections


class TimeMap:
    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        keyValues = self.map.get(key)
        if not keyValues:
            return ""
        index = self.binarySearch(keyValues, timestamp)
        return keyValues[index][1] if keyValues[index][0] <= timestamp else ""

    def binarySearch(self, keyValues, timestamp):
        start, end = 0, len(keyValues) - 1
        while start < end:
            mid = start + (end - start + 1) // 2
            if keyValues[mid][0] > timestamp:
                end = mid - 1
            else:
                start = mid
        return end
