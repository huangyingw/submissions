public class Solution
{
    public int minSubArrayLen(int s, int[] nums)
    {
        if (nums.length == 0 || nums == null)
        {
            return 0;
        }

        int left = 0, right = 0, sum = 0;
        int min = Integer.MAX_VALUE;

        while (right < nums.length)
        {
            while (sum < s && right < nums.length)
            {
                sum += nums[right++];
            }

            if (sum >= s)
            {
                min = Math.min(min, right - left);
                sum -= nums[left++];
            }
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
