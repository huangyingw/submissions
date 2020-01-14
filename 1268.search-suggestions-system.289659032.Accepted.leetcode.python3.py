import bisect
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        results = []
        for length in range(1, len(searchWord) + 1):
            prefix = searchWord[:length]
            i = bisect.bisect_left(products, prefix)
            results.append([p for p in products[i: i + 3] if p[:length] == prefix])
        return results
