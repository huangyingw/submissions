












class NumArray(object):
    def __init__(self, nums):

        self.width = int(len(nums)**0.5)
        self.bin_sums = []
        self.nums = nums
        for i, num in enumerate(nums):
            if i % self.width == 0:
                self.bin_sums.append(num)
            else:
                self.bin_sums[-1] += num

    def update(self, i, val):

        bin_i = i // self.width
        diff = val - self.nums[i]
        self.bin_sums[bin_i] += diff
        self.nums[i] = val

    def sumRange(self, i, j):

        bin_i, bin_j = i // self.width, j // self.width
        range_sum = sum(self.bin_sums[bin_i:bin_j])
        range_sum += sum(self.nums[bin_j * self.width:j + 1])
        range_sum -= sum(self.nums[bin_i * self.width:i])
        return range_sum
