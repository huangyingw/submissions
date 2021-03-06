class Solution1:
    def permuteUnique(nums):
        permutations = [[]]
        for head in nums:
            permutations = [rest[:i] + [head] + rest[i:] for rest in permutations for i in
                            range((rest + [head]).index(head) + 1)]
        return permutations


class Solution2:
    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans
