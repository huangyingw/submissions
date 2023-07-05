def numberOfLongestIncreasingSubsequences(nums):

    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    count = 0
    for i in range(n):
        if dp[i] == max(dp):
            count += 1
    return count
