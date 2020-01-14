class Solution(object):
    def minArea(self, image, x, y):
        if not image or not image[0] or image[x][y] != '1':
            return 0
        top_edge = self.find_edge(0, x, True, True, image)
        bottom_edge = self.find_edge(x + 1, len(image), True, False, image)
        left_edge = self.find_edge(0, y, False, True, image)
        right_edge = self.find_edge(y + 1, len(image[0]), False, False, image)
        return (right_edge - left_edge) * (bottom_edge - top_edge)
    def find_edge(self, left, right, column, black, image):
        while left < right:
            mid = (left + right) // 2
            if black == self.any_black(mid, column, image):
                right = mid
            else:
                left = mid + 1
        return left
    def any_black(self, i, column, image):
        if column:
            return ('1' in image[i])
        else:
            return any(image[r][i] == '1' for r in range(len(image)))
