


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = ((x + y + 1) // 2) - partitionX
            if partitionX < x and nums2[partitionY - 1] > nums1[partitionX]:
                low = partitionX + 1
            elif partitionX > 0 and nums1[partitionX - 1] > nums2[partitionY]:
                high = partitionX - 1
            else:
                if partitionX == 0:
                    maxLeft = nums2[partitionY - 1]
                elif partitionY == 0:
                    maxLeft = nums1[partitionX - 1]
                else:
                    maxLeft = max(nums1[partitionX - 1], nums2[partitionY - 1])
                if (x + y) % 2 == 1:
                    return maxLeft
                if partitionX == x:
                    minRight = nums2[partitionY]
                elif partitionY == y:
                    minRight = nums1[partitionX]
                else:
                    minRight = min(nums1[partitionX], nums2[partitionY])
                return (maxLeft + minRight) / 2
