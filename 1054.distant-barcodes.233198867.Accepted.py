


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        import heapq
        di = collections.Counter(barcodes)
        pq = [(-value, key) for key, value in di.items()]
        heapq.heapify(pq)
        result = []
        while len(pq) >= 2:
            freq1, barcode1 = heapq.heappop(pq)
            freq2, barcode2 = heapq.heappop(pq)
            result.extend([barcode1, barcode2])
            if freq1 + 1:
                heapq.heappush(pq, (freq1 + 1, barcode1))
            if freq2 + 1:
                heapq.heappush(pq, (freq2 + 1, barcode2))
        if pq:
            result.append(pq[0][1])
        return result
