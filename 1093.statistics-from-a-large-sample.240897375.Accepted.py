_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def sampleStats(self, count):

        minimum = None
        sample_count = sum(count)
        sum_samples, samples_seen = 0, 0
        mode, mode_count = 0, 0
        median_sum = 0
        median_indices = [sample_count // 2]
        if sample_count % 2 == 0:
            median_indices.append(median_indices[-1] - 1)
        for num, freq in enumerate(count):
            if freq == 0:
                continue
            if minimum is None:
                minimum = num
            maximum = num
            samples_seen += freq
            sum_samples += freq * num
            if freq > mode_count:
                mode_count = freq
                mode = num
            while median_indices and samples_seen > median_indices[-1]:
                median_sum += num
                median_indices.pop()
        mean = sum_samples / float(sample_count)
        median = median_sum / float(2 if sample_count % 2 == 0 else 1)
        return [minimum, maximum, mean, median, mode]
