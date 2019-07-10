_author_ = 'jake'
_project_ = 'leetcode'
















class Solution(object):
    def pathSum(self, nums):

        mapping = {}
        for num in nums:
            location, val = divmod(num, 10)
            depth, pos = divmod(location, 10)
            mapping[(depth, pos - 1)] = val

        def sum_paths(location, partial):
            if location not in mapping:
                return 0
            depth, pos = location
            new_partial = partial + mapping[location]
            left = (depth + 1, 2 * pos)
            right = (depth + 1, 2 * pos + 1)
            if left not in mapping and right not in mapping:
                return new_partial
            return sum_paths((depth + 1, 2 * pos), new_partial) + sum_paths((depth + 1, 2 * pos + 1), new_partial)
        return sum_paths((1, 0), 0)
