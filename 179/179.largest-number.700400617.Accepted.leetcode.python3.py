class Solution:
    def largestNumber(self, nums):
        def compare(a, b):
            return int(b + a) - int(a + b)
        nums = sorted([str(x) for x in nums], key=cmp_to_key(compare))
        ans = ''.join(nums).lstrip('0')
        return ans or '0'
