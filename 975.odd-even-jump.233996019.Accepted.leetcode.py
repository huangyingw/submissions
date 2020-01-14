class Solution:
    def oddEvenJumps(self, A):
        n = len(A)
        def next_list():
            result = [None] * n
            stack = []
            for i in indices:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        indices = sorted(range(n), key=lambda x: A[x])
        next_larger = next_list()
        indices.sort(key=lambda x: -A[x])
        next_smaller = next_list()
        odd = [False] * (n - 1) + [True]
        even = [False] * (n - 1) + [True]
        for i in range(n - 2, -1, -1):
            if next_larger[i] is not None:
                odd[i] = even[next_larger[i]]
            if next_smaller[i] is not None:
                even[i] = odd[next_smaller[i]]
        return sum(odd)
