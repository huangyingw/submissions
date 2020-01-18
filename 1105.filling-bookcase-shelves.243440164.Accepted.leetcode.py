class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        results = [0]
        for i in range(len(books)):
            width = shelf_width
            shelf_height = 0
            results.append(float("inf"))
            j = i
            while j >= 0 and width >= books[j][0]:
                shelf_height = max(shelf_height, books[j][1])
                width -= books[j][0]
                results[-1] = min(results[-1], shelf_height + results[j])
                j -= 1
        return results[-1]
