








import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []
        smallest = []
        frontier = [(nums1[0] + nums2[0], 0, 0)]
        while frontier and len(smallest) < k:
            _, i, j = heapq.heappop(frontier)
            smallest.append([nums1[i], nums2[j]])
            if len(frontier) >= k:
                continue
            if i < len(nums1) - 1:
                heapq.heappush(frontier, (nums1[i + 1] + nums2[j], i + 1, j))
            if i == 0 and j < len(nums2) - 1:
                heapq.heappush(frontier, (nums1[i] + nums2[j + 1], i, j + 1))
        return smallest
