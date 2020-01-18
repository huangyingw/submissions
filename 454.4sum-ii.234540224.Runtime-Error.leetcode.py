class Solution1:
    def fourSumCount(self, A, B, C, D):
        cnts = 0
        dd = {}
        aa = {}
        bb = {}
        cc = {}
        for a in A:
            aa[a] = aa.get(a, 0) + 1
        for b in B:
            bb[b] = bb.get(b, 0) + 1
        for c in C:
            cc[c] = cc.get(c, 0) + 1
        for d in D:
            dd[d] = dd.get(d, 0) + 1
        ab = {}
        for a, av in aa.items():
            for b, bv in bb.items():
                ab[a + b] = ab.get(a + b, 0) + av * bv
        for c, cv in cc.items():
            for d, dv in dd.items():
                if -c - d in ab:
                    cnts += ab[-c - d] * cv * dv
        return cnts


class Solution2:
    def fourSumCount(self, A, B, C, D):
        from collections import Counter
        AB = Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)
